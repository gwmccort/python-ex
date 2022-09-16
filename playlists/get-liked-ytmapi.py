''' use ytmusicapi to get list of liked songs '''

import logging as log
import csv
from ytmusicapi import YTMusic

log.basicConfig(level=log.INFO)
log.info('Starting>>>>')
ytm = YTMusic('headers_auth.json')
liked = ytm.get_liked_songs(500)

with open('data/ytm-likes.csv', 'w') as f:
    # create the csv writer
    w = csv.writer(f)
    for trk in liked['tracks']:
        log.info(f"title: {trk['title']}")
        # print('id:', trk['videoId'])
        w.writerow([trk['title'],
                    trk['artists'][0]['name']])


log.info('End:')
