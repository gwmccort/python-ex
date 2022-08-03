''' bluegrass today chart '''

# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup

BGT_URL = 'https://bluegrasstoday.com/monthly-chart/'


def get_songs():

    # blank datafram
    df = pd.DataFrame(columns=['Song', 'Artist'])

    # get url data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(BGT_URL, headers=headers)

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

    return df


url = 'https://bluegrasstoday.com/monthly-chart/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)


# %%
soup = BeautifulSoup(result.text, 'html.parser')
# tbl = soup.find('table')
tbl = soup.find('tbody')

rows = tbl.find_all('tr')

# %%
for row in rows:
    artist = row.find('strong')
    song = artist.findNext('strong')
    print(f'artist:{artist.text} song:{song.text}')

    # print('===========')
    # cols = row.find_all('td')
    # # print(f"cols length: {len(cols)}")
    # if len(cols) == 4:
    #     # print(cols[2])
    #     # print('---')
    #     artist = row.find('strong')
    #     print(f'artist:{artist.text}')
    #     song = artist.findNext('strong')
    #     print(f'song:{song.text}')

# %%
