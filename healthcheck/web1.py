import requests
import sys

proto = "https" if sys.argv[1].endswith(".dev") else "http"
host = sys.argv[1]
port = int(sys.argv[2])

print(requests.get(f"{proto}://{host}:{port}/room/0").text)
