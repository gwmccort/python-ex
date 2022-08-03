''' class to implement playlist'''

# %%
import requests
import pandas as pd
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

    URL = 'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly'
    CSV_FILE = 'data/rms_playlist.csv'

    def read(self):
        df = pd.DataFrame(columns=['Song', 'Artist'])

        req = requests.get(self.URL)
        # print(req.text)

        soup = BeautifulSoup(req.text, 'html.parser')
        # print(soup.head.title.text)  # print page title

        # read top 50 songs table
        tbl = soup.find('table')
        rows = tbl.find_all('tr')
        skip = True
        for row in rows:
            # skip first row (header)
            if skip:
                skip = False
            else:
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


class BgtPlaylist(Playlist):
    ''' bluegrass today monthly chart '''

    URL = 'https://bluegrasstoday.com/monthly-chart/'
    CSV_FILE = 'data/bgt_playlist.csv'

    def read(self):
        # print(f'RmsPlaylist.read url: {BGT_URL}')
        # return pd.DataFrame()

        # blank datafram
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


# %%
pl = RmsPlaylist()
df = pl.read()
pl.merge()
pl.write()

# %%
pl = BgtPlaylist()
df = pl.read()
pl.merge()
pl.write()

# %%
