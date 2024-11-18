import requests
import datetime as dt

USERNAME = "fatereader"
TOKEN = "25R&pe)^6*(qvQ60fnlg"
GRAPHID = "myfategraph"

# YESTERDAY = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d")

class EventTracker:
    def __init__(self):
        self.pixela_endpoint = 'https://pixe.la/v1/users'

        self.graph_endpoint = f"{self.pixela_endpoint}/{USERNAME}/graphs"

        self.pixel_endpoint = f"{self.graph_endpoint}/{GRAPHID}"

        self.header = {
            "X-USER-TOKEN": TOKEN
        }

        # self.pixel_update_endpoint = f"{self.pixel_endpoint}/{YESTERDAY}"

        # self.pixel_update = {
        #     "quantity": input(f"How much time did you spend on {TODAY}: ")
        # }

    def create_user(self):
        self.pixela_params = {}
        self.pixela_params['token'] = TOKEN
        self.pixela_params['username'] = USERNAME
        self.pixela_params['agreeTermsOfService'] = "yes"
        self.pixela_params['notMinor'] = "yes"

        self.response = requests.post(url= self.pixela_endpoint, json= self.pixela_params)
        print(self.response.text)

    def create_graph(self):
        self.graph_config = {
            "id": GRAPHID,
            "name": input("Enter your graph name: "),
            "unit": input("Enter the unit of measure[min, km, commit, etc...]: "),
            "type": "int",
            "color": "ajisai"
        }

        self.response = requests.post(url= self.graph_endpoint, json= self.graph_config, headers= self.header)
        print(self.response.text)

    def create_pixel(self):
        TODAY = dt.datetime.now().strftime("%Y%m%d")
        self.pixel_data = {
            "date": TODAY,
            "quantity": input("Enter how many minutes you have spent learning today: "),
        }

        self.response = requests.post(url= self.pixel_endpoint, json=self.pixel_data, headers= self.header)
        print(self.response.text)           

event_tracker = EventTracker()
event_tracker.create_pixel()







































# response = requests.put(url= pixel_update_endpoint, json= pixel_update, headers= header)
# print(response.text)

# response = requests.delete(url= pixel_update_endpoint, headers= header)
# print(response.text)