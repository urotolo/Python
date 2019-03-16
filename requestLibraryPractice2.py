#!/usr/bin/py

import requests

r = requests.get('https://github.com')
print(r.status_code)

# The Request library also comes with a built-in JSON decoder
# Just in case you have to deal with JSON data

r.headers
{
        'status':'200 OK',
        'content-encoding':'gzip',
        'transfer-encoding':'chunked',
        'connection':'close',
        'server':'nginx/1.0.4',
        'X-runtime':'148ms',
        'etag':'e1ca502697e5c9317743dc078f67693f',
        'content-type':'application/json;charset=utf-8'
}

print(r.headers['content-encoding'])
print(r.headers.get('Content-type'))
print(r.headers['content-type'])
print(r.headers['X-Random'])


