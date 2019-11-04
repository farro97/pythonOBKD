from flask import Flask, render_template, redirect, url_for, request
import requests
import json

app = Flask(__name__)
@app.route('/stock', methods=['GET'])
def stock():
    return render_template('stock.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    error = None
    if request.method == 'POST':
        tickerCode = request.form['stockSymbol']
        api_key = request.form['APIKey']

        url = "https://www.alphavantage.co/query"

        querystring = {"function": "TIME_SERIES_INTRADAY","symbol": tickerCode, "interval": "5min", "apikey": api_key}

        headers = {
            'cache-Control': "no-cache",
            'postman-Token': "c50d8ad2-56d2-4114-9244-6dc770d9e5c0,b7b7eaec-bdc1-453f-bd6b-96fa8ce1e741",
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        stockData = json.loads(response.text)

        lastRefreshedDate = stockData["Meta Data"]["3. Last Refreshed"]

        latestStockPrices = stockData["Time Series (5min)"][lastRefreshedDate]

        closingPrice = latestStockPrices["4. close"]

        volume = latestStockPrices["5. volume"]


    return render_template('stock_price.html', tCode=tickerCode, sPrice=closingPrice, cVolume=volume, dTime=lastRefreshedDate)
