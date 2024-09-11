import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
from alive_progress import alive_bar


def extract_links(url, keyword):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)

    keyword_links = [
        "https://www.eura2014.fi/rrtiepa/" + a["href"].lstrip("/")
        for a in links
        if keyword in a["href"]
    ]
    keyword_links = list(set(keyword_links))

    return keyword_links


def extract_data(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    description_divs = soup.find_all("div")

    data = {"URL": url}
    for div in description_divs:
        category = div.find("h2")
        if category is not None:
            category = category.text.strip()

        paragraphs = div.find_all("p")

        if category in ["1 Hanke", "2 Hakijan perustiedot"]:
            for p in paragraphs:
                if ": " in p.text:
                    key, value = p.text.split(": ", 1)
                    data[key.strip()] = value.strip()

        elif category in [
            "7 Hakemusvaiheessa ilmoitettavat arviot hankekohtaisista seurantiedoista"
        ]:

            current_ps = []
            current_h3 = None

            for tag in div.contents:
                if tag.name == "h3":
                    if current_h3 is not None:
                        data[current_h3] = " ".join(current_ps)
                    current_h3 = tag.text.strip()
                    current_ps = []
                elif tag.name == "p":
                    current_ps.append(tag.text.strip())

            if current_h3 is not None:
                data[current_h3] = " ".join(current_ps)

        elif category is not None:
            data[category] = [p.text.strip() for p in paragraphs]

    return data


def scrape_data(links) -> pd.DataFrame:

    df_list = []

    with alive_bar(len(links)) as bar:
        # count = 0
        for link in links:
            data = extract_data(link)
            df = pd.DataFrame([data], columns=data.keys())
            df_list.append(df)
            time.sleep(0.2)
            bar()
            # count += 1
            # if count >= 10:
            #     break

    result_df = pd.concat(df_list, ignore_index=True)

    return result_df
