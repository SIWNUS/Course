import os
import requests
import datetime as dt
import json
from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def percentage_difference(val1, val2):
    diff = abs(val1 - val2)
    avg = (val1 + val2) / 2
    per_diff = (diff / avg) * 100
    return round(per_diff)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Twilio API Credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_number = os.getenv("TWILIO_MY_NUMBER")

# News API Key
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Stock API Key
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
func = "TIME_SERIES_DAILY"

parameters = {
    'function': func,
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}

# STEP 1: Get Stock Data from Alpha Vantage
response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()

stock_data = response.json()

# Save stock data to a JSON file for debugging (optional)
with open("Tesla.json", 'w') as data:
    json.dump(stock_data, fp=data, indent=4, separators=(",", ":"))

today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)
diff_day = yesterday - dt.timedelta(days=1)

compare_day_1 = yesterday.strftime("%Y-%m-%d")
compare_day_2 = diff_day.strftime("%Y-%m-%d")

with open("Tesla.json") as data:
    stock_dict = json.load(fp=data)

ts_stock_data = stock_dict['Time Series (Daily)']
recent_stock_value = float(ts_stock_data[compare_day_1]['4. close'])
previous_stock_value = float(ts_stock_data[compare_day_2]['4. close'])

difference = percentage_difference(recent_stock_value, previous_stock_value)

# STEP 2: Get News Data from NewsAPI
newsapi = NewsApiClient(api_key=NEWS_API_KEY)
top_headlines = newsapi.get_top_headlines(qintitle=COMPANY_NAME, language='en', page_size=3)
sources = newsapi.get_sources()

# Save news data to a JSON file for debugging (optional)
with open("news.json", 'w') as data:
    json.dump(top_headlines, fp=data, indent=4, separators=(",", ":"))

with open("news.json") as data:
    article = json.load(fp=data)

all_article = article['articles']

client = Client(account_sid, auth_token)

# STEP 3: Send SMS if the stock price change is >= 5%
if difference >= 5:
    for article in all_article:
        headlines = article.get('title')
        brief = article.get('description', 'No description available.')
        url = article.get('url')

        if recent_stock_value > previous_stock_value:
            message = client.messages.create(
                from_=my_number,
                body=f"TSLA: 🔺{difference}%\nHeadline: {headlines}\nBrief: {brief}\nLearn more: {url}",
                to=os.getenv("TWILIO_TO_NUMBER")
            )
        elif previous_stock_value > recent_stock_value:
            message = client.messages.create(
                from_=my_number,
                body=f"TSLA: 🔻{difference}%\nHeadline: {headlines}\nBrief: {brief}\nLearn more: {url}",
                to=os.getenv("TWILIO_TO_NUMBER")
            )
        print("Message sent")
