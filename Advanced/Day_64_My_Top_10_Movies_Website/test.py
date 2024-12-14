import requests

movie_title = "The Matrix"
url = f"http://www.omdbapi.com/?t={movie_title}&apikey=91a21237"

response = requests.get(url)

data = response.json()

for key in data:
    print(key)