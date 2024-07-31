
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

all_movies = [title.getText() for title in soup.find_all(name="h3", class_="title")]
all_movies = all_movies[-1: -len(all_movies)-1: -1]

with open("./movies.txt", "w") as file:
    for movie in all_movies:
        file.write(f"{movie}\n")

