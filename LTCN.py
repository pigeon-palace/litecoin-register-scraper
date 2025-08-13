from scraper import Scraper

url = "https://www.grayscale.com/funds/grayscale-litecoin-trust"
regex = "Litecoin MWEB Balance\s+([0-9,.]+) LTC"
filename = "data/MWEB.csv"
formatter = lambda match : float(match.group(1).replace(",",""))
    
Scraper(url, regex, filename, formatter).query()
