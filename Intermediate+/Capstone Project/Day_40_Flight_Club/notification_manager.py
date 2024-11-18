import os
from twilio.rest import Client
from flight_search import FlightSearch
from smtplib import SMTP
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeZtncziQif1MmmTGwQZXcjXbbyYhpN6Md8yB6nlooXykNQ2g/viewform?usp=sf_link"

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    
    def __init__(self, list):
        self.flight = FlightSearch()

        self.list = self.flight.cheapest_flight(list)
        
        # Use environment variables for credentials
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.my_number = os.getenv("TWILIO_MY_NUMBER")
        self.my_mail = os.getenv("GMAIL_USER")
        self.my_pass = os.getenv("GMAIL_PASS")

    def send_form(self, mail):
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.my_mail, password=self.my_pass)
            message = f"Subject: The Flight Club\n\nPlease fill the attached form to subscribe!\n{GOOGLE_FORM}"
            connection.sendmail(from_addr=self.my_mail, to_addrs=mail, msg=message)
        print("form sent")

    def send_message(self):
        client = Client(self.account_sid, self.auth_token)

        for item in self.list:
            message = client.messages.create(
                from_=self.my_number,
                body=f"Low price alert! Only £{item['price']} to fly from {item['origin']} on {item['departure']} and you will reach {item['destination']} at {item['arrival']}",
                to=os.getenv("TWILIO_TO_NUMBER")
            )
        print("message sent")

    def send_mail(self, mail):
        GBP = '£'
        for item in self.list:
            with SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=self.my_mail, password=self.my_pass)
                message = (
                    f"Subject: Low Price Alert!\n\n"
                    f"Low price alert! Only {GBP}{item['price']} to fly from {item['origin']} "
                    f"on {item['departure']} and you will reach {item['destination']} at {item['arrival']} with {item['stops']} stops between."
                ).encode("utf-8")
                connection.sendmail(from_addr=self.my_mail, to_addrs=mail, msg=message)
        print("Mail sent")
