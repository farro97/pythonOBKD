from flask import Flask
import requests

url = "https://www.alphavantage.co/query"

querystring = {"function":"TIME_SERIES_INTRADAY","symbol":"MSFT","interval":"5min","apikey":"W5WVI5UJNZK2LMS1"}

payload = ""
headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "c50d8ad2-56d2-4114-9244-6dc770d9e5c0,c6225212-6bfb-4543-a91c-c880b44d1d7a",
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

app = Flask(__name__)
@app.route('/')
def home():
    return response.text