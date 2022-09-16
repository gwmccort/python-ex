''' modify date of RMS url to get more songs '''

# %%
from datetime import datetime
from datetime import timedelta

import Playlist

start_date = datetime.strptime('2022-08-27', "%Y-%m-%d")
print(start_date)

# %%
''' loop over dates scrape every week '''
# weekly by date
# 'https://www.rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly/2022-08-27'
url = 'http://rootsmusicreport.com/charts/print_chart/song/genre/bluegrass/weekly/'
date = start_date
file_name = 'data/x.csv'

for i in range(100):

    date = date - timedelta(weeks=1)
    date_string = date.strftime('%Y-%m-%d')
    pl = Playlist.RmsPlaylist(url+date_string,
                              file_name)
    pl.read()
    pl.merge()
    pl.write()
