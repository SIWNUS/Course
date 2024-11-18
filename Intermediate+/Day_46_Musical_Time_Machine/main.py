from bs4 import BeautifulSoup
import requests
import pprint

CLIENT_ID = "59cf8f9d4c6c4d10bbe80830cd10707a"
CLIENT_SECRET = "7b3e989eb6fd49d2a9f99d1537533817"

base_url = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

search_url = base_url + date

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=search_url, headers=header)

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

main_section = soup.find("main")

section_rows = main_section.find_all(name= "div", class_ = "o-chart-results-list-row-container")

song_list = []

for row in section_rows:
    title = row.find(name = "h3", id = "title-of-a-story")
    song_list.append(title.get_text().strip().replace('\n', '').replace('\t', ''))

# print(song_list)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

sp = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://example.com", scope=scope)

# token = sp.get_access_token()

user = spotipy.client.Spotify(oauth_manager=sp)

user_data = user.current_user()

user_id = user_data['id']

song_uris = []
year = date.split("-")[0]

for song in song_list:
    query = f"track:{song} year:{year}"
    results = user.search(q = query, type = "track")
    
    try:
        track = results["tracks"]["items"][0]["uri"]
        song_uris.append(track)
        print(f"'{song}' is done.")
    except IndexError:
        print(f"'{song}' cannot be found.")

new_playlist = user.user_playlist_create(user=user_id, name=f"{date} Billboard top 100", public=False, description=f"My {year} fav playlist")

# print(f"Created playlist: {new_playlist['name']} with ID: {new_playlist['id']}")

playlist_id = new_playlist['id']

# print(playlist_id)

add_tracks = user.playlist_add_items(playlist_id= playlist_id, items= song_uris)

# pprint.pp(user.user_playlist(user_id, playlist_id))