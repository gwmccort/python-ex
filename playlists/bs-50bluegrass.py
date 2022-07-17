import requests
import pandas as pd
from bs4 import BeautifulSoup


# read data from a url
# url = 'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly/2022-05-14/2022-05-14'
# r = requests.get(url)
# # print(r.text)
# html = r.text

# # write html to file
# with open('data/50bluegrass.html', 'w') as fp:
#     fp.write(html)

# read data from a file
with open('data/50bluegrass.html') as fp:
    html = fp.read()

# read html w/ bsoup
soup = BeautifulSoup(html, 'html.parser')
# print(soup.head.title.text)  # print page title

# # all the data is in the 'table'
# tbl = soup('table')
# # print(tbl)
# for td in tbl('td'):
#     print(td.text)


# for td in soup('td'):
#     print(td)

# print(soup.body.table)

# skip = True
# for tag in soup.find_all('tr'):
#     if skip:
#         skip = False
#     else:
#         print('tag:' + tag.text)

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

# write df to file as csv
df.to_csv('data/50bluegrass.csv', index=False)

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
