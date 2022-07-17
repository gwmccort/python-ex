''' read top 50 bluegrass songs from RMS rootsmusicreport.com '''

# %%
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


# get new playlist & merge with old
# %%
new_df = parse_html(read_url(BG_SONGS_URL))
old_df = pd.read_csv(BG_SONG_CSV_FILE)
m_df = merge_frames(old_df, new_df)

# save merged df
m_df.to_csv(BG_SONG_CSV_FILE, index=False)


# # # all the data is in the 'table'
# # tbl = soup('table')
# # # print(tbl)
# # for td in tbl('td'):
# #     print(td.text)

# # for td in soup('td'):
# #     print(td)

# # print(soup.body.table)

# # skip = True
# # for tag in soup.find_all('tr'):
# #     if skip:
# #         skip = False
# #     else:
# #         print('tag:' + tag.text)

# # create blank dataframe to export csv
# df = pd.DataFrame(columns=['Song', 'Artist'])

# # read top 50 songs table
# tbl = soup.find('table')
# rows = tbl.find_all('tr')
# skip = True
# for row in rows:
#     # skip first row (header)
#     if skip:
#         skip = False
#     else:
#         # create a list of songs from table & remove white space
#         cols = row.find_all('td')
#         cols = [x.text.strip() for x in cols]

#         # remove unwanted columns
#         del cols[0:3]
#         del cols[2]

#         # append to dataframe
#         df.loc[len(df)] = cols

# # write df to file as csv
# df.to_csv('data/50bluegrass.csv', index=False)

# def main():
#     # print("Hello World!")

#     html = readUrl(BG_SONGS_URL)
#     df = parseHtml(html)
#     # print(df)
#     # df.to_csv(BG_SONG_CSV_FILE)


# if __name__ == "__main__":
#     main()

# sample data
'''
<table>
<tr>
<th class="center" style="width: 20px;"></th>
<th class="center" style="width: 20px;">TW</th>
<th class="center" style="width: 20px;">LW</th>
<th>Song Title</th>
<th>Band/Artist Name</th>
<th>Sub Genre</th> </tr>
<tr>
<td class="center" style="width: 20px;"><span class="green">▲</span></td>
<td class="center" style="width: 20px;">1</td>
<td class="center" style="width: 20px;">3</td>
<td>Beside Myself</td>
<td><a href="/bands/view/5470/yonder-mountain-string-band">Yonder Mountain String Band</a></td>
<td><a href="/charts/view/album/sub_genre/contemporary-bluegrass/weekly">Contemporary Bluegrass</a></td>
</tr>
<tr>
<td class="center" style="width: 20px;"><span class="red">▼</span></td><td class="center" style="width: 20px;">2</td><td class="center" style="width: 20px;">1</td><td>Hard Line</td><td><a href="/bands/view/464/the-infamous-stringdusters">The Infamous Stringdusters</a></td><td><a href="/charts/view/album/sub_genre/contemporary-bluegrass/weekly">Contemporary Bluegrass</a></td></tr><tr><td class="center" style="width: 20px;"><span class="red">▼</span></td><td class="center" style="width: 20px;">3</td><td class="center" style="width: 20px;">2</td><td>I Wish I Had a Lifeline</td><td><a href="/bands/view/96518/stoney-creek-bluegrass-band">Stoney Creek Bluegrass Band</a></td><td><a href="/charts/view/album/sub_genre/contemporary-bluegrass/weekly">Contemporary Bluegrass</a></td></tr><tr><td class="center" style="width: 20px;"><span class="green">▲</span></td><td class="center" style="width: 20px;">4</td><td class="center" style="width: 20px;">11</td><td>There is a Time</td>
'''

# %%
