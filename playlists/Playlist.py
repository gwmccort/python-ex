''' class to implement playlist '''
# T2D: get old rms playlist

# %%
# import re

import pandas as pd
import requests
from bs4 import BeautifulSoup


class Playlist:
    ''' abstrace playlist class'''

    URL = None
    CSV_FILE = None

    def __init__(self):
        self._playlist = None

    @property
    def playlist(self):
        '''playlist getter'''
        return self._playlist

    @playlist.setter
    def playlist(self, dataframe):
        print('Setting playlist')
        self._playlist = dataframe

    def read(self):
        print('Playlist.read')
        pass

    def write(self):
        self._playlist.to_csv(self.CSV_FILE, index=False)

    def merge(self):
        old_df = pd.read_csv(self.CSV_FILE)

        df = pd.concat([self._playlist, old_df]).drop_duplicates()
        df = df.reset_index(drop=True)

        self._playlist = df
        return df


class RmsPlaylist(Playlist):
    ''' read top 50 bluegrass songs from RMS rootsmusicreport.com '''

    # weekly by date
    #     'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly/2022-08-27'
    # subgenre
    #      https://www.rootsmusicreport.com/charts/print_chart/song/sub_genre/contemporary-bluegrass/weekly/2022-09-03/2022-09-03
    # yearly
    #      https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/yearly/2021
    URL = 'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly'
    CSV_FILE = 'data/rms_playlist.csv'

    def read(self):
        df = pd.DataFrame(columns=['Song', 'Artist'])
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        # read top 50 songs table
        rows = soup.find('table').find_all('tr')

        # skip first row (header)
        for row in rows[1:]:
            # create a list of songs from table & remove white space
            cols = row.find_all('td')
            cols = [x.text.strip() for x in cols]

            # remove unwanted columns
            del cols[0:3]
            del cols[2]

            # append to dataframe
            df.loc[len(df)] = cols

        self._playlist = df
        return df

    def __init__(self):
        Playlist.__init__(self)

    def __init__(self, url, file):
        self.URL = url
        self.CSV_FILE = file
        super().__init__()


class BgtPlaylist(Playlist):
    ''' bluegrass today monthly chart '''

    URL = 'https://bluegrasstoday.com/monthly-chart/'
    CSV_FILE = 'data/bgt_playlist.csv'

    def read(self):
        df = pd.DataFrame(columns=['Song', 'Artist'])

        # get url data
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        result = requests.get(self.URL, headers=headers)

        soup = BeautifulSoup(result.text, 'html.parser')
        rows = soup.find('tbody').find_all('tr')

        for row in rows:
            # print('========================')
            new_row = []
            artist = row.find('strong')
            song = artist.findNext('strong')
            # print(f'artist:{artist.text} song:{song.text}')

            df.loc[len(df)] = [song.text, artist.text]

            # list_row = ["Hyperion", 27000, "60days", 2000]
            # df.loc[len(df)] =

        self._playlist = df
        return df

    def __init__(self):
        Playlist.__init__(self)


class GooglePlaylist(Playlist):
    ''' google music search playlist '''
    # best bluegrass
    # URL = "https://www.google.com/search?q=best+all+time+bluegrass+songs"
    # FILE = "data/Best Bluegrass.csv"

    URL = "https://www.google.com/search?q=The+Po%E2%80%99+Ramblin%E2%80%99+songs"
    FILE = "data/poboys.csv"

    # best jam bands
    # URL = "https://www.google.com/search?q=best+jam+band+songs"
    # FILE = "data/Best Jam Band.csv"

    def read(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        songs = pd.DataFrame(columns=['Song', 'Artist'])

        entries = soup.find_all('div', {'class': 'X7NTVe'})
        for entry in entries:
            song = entry.find('h3').text
            artist = entry.find(
                'div', {'class': 'BNeawe tAd8D AP7Wnd'}
            ).text
            artist = re.sub(r'\d*$', '', artist)
            songs.loc[len(songs)] = [song, artist]

        self._playlist = songs
        return songs


class ApplePlaylist(Playlist):
    # bluegrass best known songs
    # URL = "https://music.apple.com/us/playlist/bluegrass-jukebox-best-known-songs/pl.1bae268778d14d18a3951362e7e059a5"
    # FILE = 'data/apple-best-bluegrass.csv'

    # classic rock
    URL = "https://music.apple.com/us/playlist/classic-rock-essentials/pl.1a7fd42205674dd282d106f533f4bea6"
    FILE = 'data/apple-classic-rock.csv'

    def read(self):
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        songs = pd.DataFrame(columns=['Song', 'Artist'])

        entries = soup.find_all(
            'div', {'class': "songs-list__col songs-list__col--song typography-body"})

        for e in entries:
            song = e.find('div', {'class': "songs-list-row__song-name"}).text
            artist = e.find(
                'div', {'class': "songs-list-row__by-line"}).find('span').text
            # remove blanks & new lines
            artist = " ".join(artist.split()).strip()

            # append to dataframe
            songs.loc[len(songs)] = [song, artist]

        self._playlist = songs
        return songs
