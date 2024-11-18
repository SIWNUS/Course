import requests
import time
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_URL = "https://api.sheety.co/101395310503c1b9c9f180d6c137f6e5/flightDeals/prices"
        self.TOKEN = "Bearer fv@@A(4*0UT#yP!8oT"

        self.flight = FlightSearch()
        
        self.SHEETY_USERS = "https://api.sheety.co/101395310503c1b9c9f180d6c137f6e5/flightDeals/users"

    def get_data(self):
        headers_param = {
            'Content-Type': 'application/json',
            "Authorization": self.TOKEN
        }

        response = requests.get(url= self.SHEETY_URL, headers= headers_param)
        sheet_data = response.json()

        return sheet_data['prices']
    
    def write_data(self):
        data = self.get_data()

        for item in data:
            city = item['city']
            id = item['id']

            if item['iataCode'] == '':
                item['iataCode'] = self.flight.city_search(city)
                body = {
                    "price": {
                        "iataCode": item['iataCode'],
                    }
                }

                url = f"https://api.sheety.co/101395310503c1b9c9f180d6c137f6e5/flightDeals/prices/{id}"

                head = {
                    'Content-Type': 'application/json',
                    "Authorization": self.TOKEN
                }

                write_response = requests.put(url= url, headers= head, json= body)
                time.sleep(2)

    def get_users(self):
        headers_param = {
            'Content-Type': 'application/json',
            "Authorization": self.TOKEN
        }

        response = requests.get(url= self.SHEETY_USERS, headers= headers_param)
        user_data = response.json()
        return user_data['users']
