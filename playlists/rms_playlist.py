''' read top 50 bluegrass songs from RMS rootsmusicreport.com '''

import requests
import pandas as pd
from bs4 import BeautifulSoup

BG_SONGS_URL = 'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly'
BG_SONG_FILE = 'data/50bluegrass.html'
BG_SONG_CSV_FILE = 'data/50bluegrass.csv'


def read_url(url):
    ''' read data from a url '''
    r = requests.get(url)
    # # print(r.text)
    return r.text


def read_file(fname):
    ''' read data from a file '''

    with open(fname) as fp:
        return fp.read()


def write_file(fname, html):
    ''' write html to file '''

    with open(fname, 'w') as fp:
        fp.write(html)


def merge_frames(old_df, new_df):
    ''' merge 2 dataframes and drop duplicates '''

    # merge & drop duplicates
    m_df = pd.concat([new_df, old_df]).drop_duplicates()
    m_df = m_df.reset_index(drop=True)
    return m_df


def parse_html(html):
    ''' read root music html w/ bsoup '''
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.head.title.text)  # print page title

    # create blank dataframe to export csv
    df = pd.DataFrame(columns=['Song', 'Artist'])

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
    return df


def merge_latest(url, fname):
    ''' merge latest chart with saved data '''
    new_df = parse_html(read_url(url))
    old_df = pd.read_csv(fname)
    m_df = merge_frames(old_df, new_df)

    # save merged df
    m_df.to_csv(BG_SONG_CSV_FILE, index=False)


def main():
    merge_latest(BG_SONGS_URL, BG_SONG_CSV_FILE)


if __name__ == "__main__":
    main()
