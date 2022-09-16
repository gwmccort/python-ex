''' upload playlist to ytm '''

import logging
import sys
import csv
from ytmusicapi import YTMusic

import logging_tree
from logging_tree import printout

# IN_CSV = 'data/bgt_playlist.csv' # works
IN_CSV = 'data/delete-me.csv'
# 130+ songs fail
# IN_CSV = 'data/rms_playlist.csv'
# IN_CSV = 'data/big-rms-bluegrass.csv'

# config log
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# logging.basicConfig()

# print logging tree
with open('no-cfg.txt', 'a') as fp:
    fp.write(logging_tree.format.build_description())
# printout()

# logging.basicConfig(
#     # filename='ytm.log',
#     #                 filemode='a',
#     # format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#     # datefmt='%m-%d %H:%M'
# )

# printout()
# print('--------------------------------')

# log = logging.getLogger()
# log = logging.getLogger('ytm')
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# console log
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(levelname)-8s %(message)s')
ch.setFormatter(formatter)

# file log
fh = logging.FileHandler('ytm.log')
fh.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     # '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s')
#     '%(levelname)-8s %(message)s')
fh.setFormatter(formatter)

log.addHandler(ch)
log.addHandler(fh)

# write logging cfg tree
with open('after-cfg.txt', 'a') as fp:
    fp.write(logging_tree.format.build_description())
# printout()
# print('--------------------------------')

# log.basicConfig(filename='ytm-log.txt',
#                 level=log.INFO)
# log.basicConfig(level=log.INFO)
# log.basicConfig(level=log.DEBUG)

# def configLog():
#     log = logging.getLogger("mylog")
#     formatter = logging.Formatter(
#         '%(asctime)s | %(name)s |  %(levelname)s: %(message)s')
#     log.setLevel(logging.DEBUG)

#     stream_handler = logging.StreamHandler()
#     stream_handler.setLevel(logging.INFO)
#     stream_handler.setFormatter(formatter)

#     logFilePath = "my.log"
#     file_handler = log.handlers.TimedRotatingFileHandler(
#         filename=logFilePath, when='midnight', backupCount=30)
#     file_handler.setFormatter(formatter)
#     file_handler.setLevel(logging.DEBUG)

#     log.addHandler(file_handler)
#     log.addHandler(stream_handler)

###################################
# configLog()
log.info('START >>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ytm = YTMusic('headers_auth.json')

# read csv data
with open(IN_CSV) as fp:
    reader = csv.reader(fp)
    songs = list(reader)

# swap song & artist columns
for song in songs:
    song[0], song[1] = song[1], song[0]
log.debug(f'data; {songs}')

# # write csv data
# with open('data/x.csv', 'w') as fp:
#     writer = csv.writer(fp)
#     writer.writerows(songs)

# combine title & artist
songs = []
for i in songs:
    songs.append(' - '.join(i))
log.debug(songs)


log.warning('END: quitting @ #88')
quit()


# get list of song id's
plIds = []
# skip first
for s in songs[1:]:
    sr = ytm.search(s, filter='songs', limit=1)
    log.debug(f'sr len: {len(sr)} sr: {sr}')

    if (len(sr) > 0):
        sid = sr[0]['videoId']
        # log.info(f'songId: {sid}')
        plIds.append(sid)
log.debug(plIds)


# add song one at a time
# plid = ytm.create_playlist('ytmapi test', 'test description')
# log.info(f'plid: {plid}')
# for z in plIds:
#     r = ytm.add_playlist_items(plid, videoIds=[z])
#     print(f'r: {r}')

# create a new playlist via list of id's
plid = ytm.create_playlist('ytmapi test', 'test description')
log.info(f'plid: {plid}')

# add songs to playlist
r = ytm.add_playlist_items(plid, plIds)
log.warning(f"status: {r['status']}")
log.info(f'r: {r}')

log.info('Done:')
quit()


# %%
''' add a song to pl '''
sr = ytm.search('billy strings - red dazy')
ytm.add_playlist_items(plid, [sr[0]['videoId']])
for song in songs:
    sr = ytm.search(song, filter='songs')
    sid = sr[0]['videoId']
    log.info(f'song: {song} songId: {sid}')
    plIds.append(sid)

ytm.add_playlist_items(plid, plIds)


# %%
''' add list of songs '''
songs = [
    "I Ain't Dead Yet",
    'Old Number Seven',
    'Old and in the way',
    'watch it fall, billy strings']
plIds = []

for s in songs:
    sr = ytm.search(s, filter='songs')
    sid = sr[0]['videoId']
    log.info(f'songId: {sid}')
    plIds.append(sid)

ytm.add_playlist_items(plid, plIds)


# %%
