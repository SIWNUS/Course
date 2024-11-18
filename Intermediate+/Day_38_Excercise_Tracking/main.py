import requests
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv(".env")

api_url = os.getenv("API_ENDPOINT")

api_headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
}
api_params = {
    "query": input("What exercise did you do today? ")
}

response = requests.post(url= api_url, json= api_params, headers= api_headers)

response_dict = response.json()

exercise_list = response_dict["exercises"][0]


sheet_params = {
    "workout": {
        "date": dt.datetime.now().strftime("%d/%m/%Y"),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise_list["name"],
        "duration": exercise_list["duration_min"],
        "calories": exercise_list["nf_calories"],
    }
}

sheety_url = os.getenv("SHEETY_ENDPOINT")

headers_param = {
    'Content-Type': 'application/json',
    "Authorization": os.getenv("TOKEN")
}

sheet_response = requests.post(url= sheety_url, json= sheet_params, headers=headers_param)
print(sheet_response.status_code)
print(sheet_response.json())
