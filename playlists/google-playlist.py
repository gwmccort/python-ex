''' scrap google song list'''
# %%
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# URL = "https://www.google.com/search?q=best+all+time+bluegrass+songs"
# FILE = "data/Best Bluegrass.csv"

URL = "https://www.google.com/search?q=best+jam+band+songs"
FILE = "data/Best Jam Band.csv"

req = requests.get(URL)

# with open("data/x.html", "w") as fp:
#     fp.write(req.text)

soup = BeautifulSoup(req.text, 'html.parser')
# with open("data/xx.html", "w") as fp:
#     fp.write(soup.prettify())

songs = pd.DataFrame(columns=['Song', 'Artist'])

entries = soup.find_all('div', {'class': 'X7NTVe'})
for entry in entries:
    song = entry.find('h3').text
    artist = entry.find(
        'div', {'class': 'BNeawe tAd8D AP7Wnd'}
    ).text
    artist = re.sub(r'\d*$', '', artist)
    # print(f'song: {song} artist: {artist}')
    songs.loc[len(songs)] = [song, artist]

songs.to_csv(FILE, index=False)

# %%
