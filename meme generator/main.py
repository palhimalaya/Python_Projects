import os

import requests

url = "https://memes.blademaker.tv/api?lang=en"
response = requests.get(url)
response.raise_for_status()
data = response.json()
meme = data["image"]
print(meme)

