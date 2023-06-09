#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

MOVIES_ENDPOINT = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
MOVIES_FILE = "greatest_movies.txt"

response = requests.get(MOVIES_ENDPOINT, timeout=5)

soup = BeautifulSoup(response.text, "html.parser")

movie_title = soup.find_all(name="h3", class_="title")
movie_title.reverse()

with open(MOVIES_FILE, 'w') as file:
    for title in movie_title:
        file.write(f'{title.getText()}\n')


