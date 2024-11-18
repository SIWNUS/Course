import os
from twilio.rest import Client
from flight_search import FlightSearch
from dotenv import load_dotenv

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self):
        self.flight = FlightSearch()

        # Load environment variables from .env file
        load_dotenv()

        # Access Twilio credentials from environment variables
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.my_number = os.getenv("TWILIO_MY_NUMBER")
        self.to_number = os.getenv("TWILIO_TO_NUMBER")

    def send_message(self, list):
        client = Client(self.account_sid, self.auth_token)

        # Fetch flight offer details
        dlist = self.flight.flight_offer_search(list)

        # Send message for each item in the list
        for item in dlist:
            message = client.messages.create(
                from_=self.my_number,
                body=f"Low price alert! Only £{item['price']} to fly from {item['origin']} on {item['departure']} and you will reach {item['destination']} at {item['arrival']}",
                to=self.to_number
            )
