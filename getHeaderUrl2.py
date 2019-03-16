#!/usr/bin/py

import json
import requests

url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
headers = {'content-type':'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
r1 = requests.get('http://github.com')

"""print(r1.url)
print(r1.status_code)
print(r1.history)
"""

r2 = requests.post("http://httpbin.org/post")

#print(r2)

