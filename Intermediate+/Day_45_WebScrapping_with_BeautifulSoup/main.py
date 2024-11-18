from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-anime-movies/")

contents = response.text

soup = BeautifulSoup(contents, "html.parser")

main_content = soup.find("main")

articles = main_content.find("article")

titles = articles.find_all("h2")

for title in titles[::-1]:
    with open("Top Anime List.txt", "a") as fp:
        fp.write(title.get_text(separator = "\n"))
        fp.write("\n")
    
