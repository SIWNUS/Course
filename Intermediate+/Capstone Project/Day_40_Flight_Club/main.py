#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.de
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight = FlightSearch()
data = DataManager()

dlist = data.get_data()

alert = NotificationManager(dlist)

new_mail = input("Enter your mail id: ")

alert.send_form(new_mail)

# alert.send_message()

users = data.get_users()

for user in users:
    mail = user['whatIsYourEmail?']
    alert.send_mail(mail)
