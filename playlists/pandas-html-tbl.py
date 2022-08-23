''' read html with pandas '''

# %%
import requests
import pandas as pd

# %%
''' read bgt top songs with pandas & requests to avoid 403 '''

url = 'https://bluegrasstoday.com/top-30-bluegrass-songs-of-2020/'
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
req = requests.get(url, headers=header)

# set col header's from 1st row
dfs = pd.read_html(req.text, header=0)
songs = dfs[0][['ARTIST', 'TITLE']]

# write songs to txt file
with open('data/x.txt', 'w') as f:
    for idx in songs.index:
        f.write(f"{songs['ARTIST'][idx]} - {songs['TITLE'][idx]}\n")

# write csv file
songs.to_csv('data/x.csv', index=False)
songs

# %%
''' read wiki html table with pandas w/o requests from https://blog.finxter.com/how-to-read-html-tables-with-pandas '''

tables = pd.read_html(
    'https://en.wikipedia.org/wiki/Python_(programming_language)')
# Number of tables: 13
print(f'Number of tables: {len(tables)}')
tbl0 = tables[0]
tbl0

# %%
''' read rms bluegrass '''

URL = 'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly'
tbls = pd.read_html(URL)
df = tbls[0]
songs = df[['Song Title', 'Band/Artist Name']]

# rename cols & write to csv
songs = songs.rename(
    columns={'Song Title': 'Title', 'Band/Artist Name': 'Artist'})
songs.to_csv('data/x.csv', index=False)

# write csv file & rename col headers
# songs.to_csv('data/x.csv', header=['Title', 'Artist'], index=False)

songs
