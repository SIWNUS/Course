import requests

gender_response = requests.get(url="https://api.genderize.io?name=micky")
content = gender_response.json()
print(content["gender"])