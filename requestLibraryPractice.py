#!/usr/bin/py

import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

elementTypes = [type(item) for item in list(soup.children)]
html = list(soup.children)[2]

"""
print(elementTypes)
print("\n")
print(html)
print("\n")
print(list(html.children))
"""

body = list(html.children)[3]
p = list(body.children)[1]

print(p.get_text())
print("\n")

soupObj2 = BeautifulSoup(page.content, 'html.parser')
print(soupObj2.find_all('p')[0].get_text())

soupObj3 = BeautifulSoup(page.content, 'html.parser')
print(soupObj3.find('p'))
