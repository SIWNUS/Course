import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenWeather API
API_KEY = os.getenv("OPENWEATHER_API_KEY")
lat = 11.2997
lon = 76.9349
TIMESTAMP = 4

parameters = {
    'lat': lat,
    'lon': lon,
    'cnt': TIMESTAMP,
    'appid': API_KEY,
    'units': 'metric'
}

# Twilio API credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_number = os.getenv("TWILIO_MY_NUMBER")
to_number = os.getenv("TWILIO_TO_NUMBER")

# API Integration
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_data_list = weather_data['list']

prob = 0
will_rain = False
for ts in weather_data_list:
    if ts['weather'][0]['id'] < 700:  # ID less than 700 indicates rain
        prob = ts['pop']
        will_rain = True

client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages.create(
        from_=my_number,
        body=f'Rain probability: {prob}\nBring your umbrella today!!!',
        to=to_number
    )

    print(message.status)  # Prints message status to confirm it's sent
else:
    print("No rain forecasted today.")
