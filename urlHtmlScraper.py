#!/usr/bin/py

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soupObj1 = BeautifulSoup(page.content, 'html.parser')

print(soupObj1.find_all(id="first")) # Finds all p tags under the class called "outer-text"


