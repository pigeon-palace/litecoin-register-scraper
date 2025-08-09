import requests
from bs4 import BeautifulSoup
import re
import time
import csv

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"}
class Scraper():
    def __init__(self, _url, _regex, _filename, _formatter):
        self.url = _url
        self.regex = _regex
        self.filename = _filename
        self.formatter = _formatter

    def query(self):
        print("Requesting:", self.url)
        response = requests.get(self.url, headers=HEADERS)
        print("Parsing...")
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Matching...")
        match = re.search(self.regex, soup.text)
        with open(self.filename, "a+") as f:
            writer = csv.writer(f)
            writer.writerow([time.time(), self.formatter(match)])
        print("Finished!")
    
