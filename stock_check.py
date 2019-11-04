from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)
@app.route('/stock',methods=['GET'])
def stock():
    return render_template('stock.html')

@app.route('/result',methods=['GET', 'POST'])
def result():
    error = None
    if request.method == 'POST':
        tickerCode = request.form['stockSymbol']
        api_key = request.form['APIKey']
        url = "https://www.alphavantage.co/query"

        querystring = {"function":"TIME_SERIES_INTRADAY","symbol":tickerCode,"interval":"5min","apikey":api_key}

        payload = ""
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "c50d8ad2-56d2-4114-9244-6dc770d9e5c0,b7b7eaec-bdc1-453f-bd6b-96fa8ce1e741",
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        return response.text