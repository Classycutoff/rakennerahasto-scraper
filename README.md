# rakennerahasto-scraper

Kerää dataa EURA-hankkeiden tietopalvelun verkkosivustolta https://www.eura2014.fi/rrtiepa/ ja tekee datasta pandas dataframen.

Käyttö:

extract_links kerää kaikki halutun sanan sisältävät linkit verkkosivulta. Tietopalvelu listaa kätevästi kaikkien projektien linkit samalle sivulle, ja ne sisältävät termin "projektikoodi"

Kerää kaikki projektilinkit
`links = extract_links('https://www.eura2014.fi/rrtiepa/projektilista.php?rahasto=ALL', 'projektikoodi')`

Kerätään jokaisesta linkistä projektin tiedot ja tallennetaan pandas dataframe -taulukkoon.

`projektidata = scrape_data(links)`
