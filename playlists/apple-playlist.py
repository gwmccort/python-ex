''' scrap apple song list '''

# %%

import requests
from bs4 import BeautifulSoup
import pandas as pd

# bluegrass best known songs
# URL = "https://music.apple.com/us/playlist/bluegrass-jukebox-best-known-songs/pl.1bae268778d14d18a3951362e7e059a5"
# FILE = 'data/apple-best-bluegrass.csv'

# classic rock
URL = "https://music.apple.com/us/playlist/classic-rock-essentials/pl.1a7fd42205674dd282d106f533f4bea6"
FILE = 'data/apple-classic-rock.csv'

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
# with open("apple.html", "w") as fp:
#     fp.write(soup.prettify())

songs = pd.DataFrame(columns=['Song', 'Artist'])
entries = soup.find_all(
    'div', {'class': "songs-list__col songs-list__col--song typography-body"})

with open("apple.txt", "w") as fp:

    for e in entries:
        song = e.find('div', {'class': "songs-list-row__song-name"}).text
        artist = e.find(
            'div', {'class': "songs-list-row__by-line"}).find('span').text
        # remove blanks & new lines
        artist = " ".join(artist.split()).strip()

        # append to dataframe
        songs.loc[len(songs)] = [song, artist]

# %%
songs.to_csv(FILE, index=False)

# %%
