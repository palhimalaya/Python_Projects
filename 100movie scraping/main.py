import requests
from bs4 import BeautifulSoup
import html

response = requests.get(url="https://www.timeout.com/newyork/movies/best-movies-of-all-time")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
data = soup.find_all(name="a", class_="xs-text-charcoal decoration-none")

movie_name = [name.getText().split("\n")[1].strip().replace("\xa0", "") for name in data]
print("movie_name")
with open("100movies.txt", "w") as file:
    for n in range(100):
        file.write(f"{movie_name[n]}\n")
