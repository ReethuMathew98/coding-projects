# importing the required modules
from bs4 import BeautifulSoup
import requests

# Getting the content from the website
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
empire_website = response.text

# Scraping the list of movies from the content
soup = BeautifulSoup(empire_website, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
movies = []
for movie in movie_titles:
    movies.append(movie.getText())
  
# Reversing the list to get the movies from 1-100
movies.reverse()

# Writing the output file
with open('movies.txt', 'w', encoding='UTF-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
