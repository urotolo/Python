#!/usr/bin/py

import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.dataquest.io/blog/web-scraping-tutorial-python/https://www.dataquest.io/blog/web-scraping-tutorial-python/")
print(url.headers, url.status_code)

print("\n")
print("\n")
print("\n")

soupObj1 = BeautifulSoup(url.content, 'html.parser')
print(soupObj1.find_all('p'))
