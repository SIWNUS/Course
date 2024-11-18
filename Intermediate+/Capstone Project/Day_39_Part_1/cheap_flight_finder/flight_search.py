import requests
import datetime as dt
from flight_data import FlightData

TODAY = dt.datetime.now()
RETURN_DATE = TODAY + dt.timedelta(days= (6*30))

class FlightSearch:
    def __init__(self):
        self.API_KEY = "y4AoCPmBOH9vHcJln44Exujw8vLfNiFc"
        self.API_SECRET = "4EeNaUYMGtHTcqYC"

        self.API_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

        self.API_TOKEN = self.get_auth_token()

        self.FLIGHT_API_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

        self.CITY_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


    def get_auth_token(self):
        token_param = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }

        API_HEADER = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        flight_response = requests.post(url = self.API_URL, data=token_param, headers=API_HEADER)
        flight_response.raise_for_status()
        return flight_response.json()['access_token']
    
    def city_search(self, city):
        city_body = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }

        headers = {"Authorization": f"Bearer {self.API_TOKEN}"}

        city_response = requests.get(url= self.CITY_URL, headers=headers, params= city_body)
        city_data = city_response.json()

        code = city_data["data"][0]['iataCode']

        return code

    
    def flight_offer_search(self, destinations):
        header = {
            "Authorization": f"Bearer {self.API_TOKEN}",
            "Content-Type": "application/json"
        }
        final_offers = []

        for item in destinations:
            prices = []  # Initialize prices for each destination
            cheapest_flight_data = None  # Variable to hold data of the cheapest flight

            for i in range(180):
                target_date = TODAY + dt.timedelta(days=i)
                constraint = { 
                    "currencyCode": "GBP", 
                    "originDestinations": [
                        { 
                            "id": "1", 
                            "originLocationCode": "LON", 
                            "destinationLocationCode": item['iataCode'], 
                            "departureDateTimeRange": {"date": target_date.strftime("%Y-%m-%d")},
                        } 
                    ], 
                    "travelers": [ 
                        { 
                            "id": "1", 
                            "travelerType": "ADULT" 
                        } 
                    ], 
                    "sources": ["GDS"],
                    "searchCriteria": { 
                        "maxFlightOffers": 2, 
                        "flightFilters": { 
                            "cabinRestrictions": [ 
                                { 
                                    "cabin": "BUSINESS", 
                                    "coverage": "MOST_SEGMENTS", 
                                    "originDestinationIds": ["1"] 
                                }
                            ]
                        } 
                    } 
                }

                response = requests.post(self.FLIGHT_API_URL, headers=header, json=constraint)

                if response.status_code == 200:
                    result = response.json().get('data', [])
                    if result:
                        for flight in result:
                            price = float(flight['price']['grandTotal'])
                            prices.append(price)

                            # Check if this is the cheapest flight so far
                            if cheapest_flight_data is None or price < cheapest_flight_data['price']:
                                cheapest_flight_data = {
                                    'price': price,
                                    'origin': flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                                    'dest': flight["itineraries"][0]["segments"][-1]["arrival"]["iataCode"],
                                    'dept_time': flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
                                    'arr_time': flight["itineraries"][0]["segments"][-1]["arrival"]["at"].split("T")[0]
                                }

                print(f"Checked day {i + 1}")

            # After collecting all prices, check for the cheapest
            if cheapest_flight_data and cheapest_flight_data['price'] < item['lowestPrice']:
                di = FlightData(cheapest_flight_data['price'], 
                                cheapest_flight_data['origin'], 
                                cheapest_flight_data['dest'], 
                                cheapest_flight_data['dept_time'], 
                                cheapest_flight_data['arr_time'])
                final_offers.append(di.dict)

        return final_offers
