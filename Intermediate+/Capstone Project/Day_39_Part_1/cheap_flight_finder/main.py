#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.de
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


flight = FlightSearch()
data = DataManager()
alert = NotificationManager()

list = data.get_data()

alert.send_message(list)

