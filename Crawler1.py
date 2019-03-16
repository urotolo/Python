#!/usr/bin/py

import requests
from bs4 import BeautifulSoup

url = requests.get("http://www.espn.com")
soupObj1 = BeautifulSoup(url.content, 'html.parser')

#print(soupObj1.select("div p"))
print(url.headers, url.status_code)

