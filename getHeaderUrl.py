#!/usr/bin/py

import requests

# Get the headers of a given URL
resp = requests.head("http://www.google.com")
print(resp.status_code, resp.headers)
print(resp.encoding)
