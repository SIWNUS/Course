from bs4 import BeautifulSoup
import requests
from clr_scrn import clr_screen

root_url = "https://genius.com/"

song = input("Song title: ").lower().replace(" ","-")
singer = input("Singer of the song: ").lower().replace(" ","-")

attr = singer + "-" + song + "-lyrics"

url = root_url + attr

response = requests.get(url)
response.raise_for_status()

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

lyric_div = soup.find_all("div", attrs={"data-lyrics-container": "true"})
lines = []
clr_screen()
for div in lyric_div:
    all_lines = div.get_text(separator="\n").splitlines()
    for line in all_lines:
        print(line)
        print()
    print("\n\n")