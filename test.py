from flask import Flask
import requests

app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Welcome to OBKD Subject</h1>"