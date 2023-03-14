import requests
import sys

proto = "https" if sys.argv[1].endswith(".dev") else "http"
host = sys.argv[1]
port = int(sys.argv[2])

headers = {'User-Agent': 'lyonbrowser', 'Referer': 'https://maclyonsden.com/', 'Date': 'Tue, 1 Jan 2069 00:00:00 GMT', 'Upgrade-Insecure-Requests': '1', 'Downlink': '16900'}
print(requests.get(f"{proto}://{host}:{port}/", headers=headers).text)
