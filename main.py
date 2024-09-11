import time
import pandas as pd
from utils.scraper import extract_links, scrape_data


def main():
    print("Extracting links...")
    links = extract_links(
        "https://www.eura2014.fi/rrtiepa/projektilista.php?rahasto=ALL", "projektikoodi"
    )
    print("Links extracted... Starting to scrape data.")
    projektidata = scrape_data(links)
    projektidata.to_csv("data/projektidata.csv")


if __name__ == "__main__":
    start = time.time()
    main()
    print(f"Program took: {round(time.time() - start, 3)} s.")
