import requests
import datetime as dt

USERNAME = "fatereader"
TOKEN = "25R&pe)^6*(qvQ60fnlg"
TODAY = dt.datetime.now().strftime("%Y%m%d")
YESTERDAY = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d")

pixela_endpoint = 'https://pixe.la/v1/users'

pixela_params = {}
pixela_params['token'] = TOKEN
pixela_params['username'] = "fatereader"
pixela_params['agreeTermsOfService'] = "yes"
pixela_params['notMinor'] = "yes"

# response = requests.post(url= pixela_endpoint, json= pixela_params)

# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "myfategraph1",
    "name": "Course Learning Graph",
    "unit": "commit",
    "type": "int",
    "color": "kuro"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url= graph_endpoint, json= graph_config, headers= header)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

pixel_data = {
    "date": TODAY,
    "quantity": input("Enter how many minutes you have spent learning today: "),
}

response = requests.post(url= pixel_endpoint, json=pixel_data, headers= header)
print(response.text)

pixel_update_endpoint = f"{pixel_endpoint}/{YESTERDAY}"

# pixel_update = {
#     "quantity": input(f"How much time did you spend on {TODAY}: ")
# }

# response = requests.put(url= pixel_update_endpoint, json= pixel_update, headers= header)
# print(response.text)

# response = requests.delete(url= pixel_update_endpoint, headers= header)
# print(response.text)