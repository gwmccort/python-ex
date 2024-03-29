''' upload playlist to ytm '''

import logging
import time
import sys
import csv
from ytmusicapi import YTMusic

import logging_tree
from logging_tree import printout

start_time = time.time()

# IN_CSV = 'data/bgt_playlist.csv' # works
# IN_CSV = 'data/delete-me.csv' #25
# 130+ songs fail due to duplicate id's
# IN_CSV = 'data/rms_playlist.csv'
IN_CSV = 'data/big-rms-bluegrass.csv'


def configLogging():
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
    return log


def readSongs(IN_CSV, log):
    # read csv data
    with open(IN_CSV) as fp:
        reader = csv.reader(fp)
        songs = list(reader)

    # TODO: change cvs column order?
    # swap song & artist columns
    for song in songs:
        song[0], song[1] = song[1], song[0]
    log.debug(f'songs: {songs}')
    return songs


def writeCsv(songs):
    # write csv data
    with open('data/x.csv', 'w') as fp:
        writer = csv.writer(fp)
        writer.writerows(songs)


def getSongIds(log, ytm, songsSearch):
    # get list of song id's
    plIds = []
# skip first
    for s in songsSearch[1:]:
        sr = ytm.search(s, filter='songs', limit=1)
        # log.debug(f'sr len: {len(sr)} sr: {sr}')

        if (len(sr) > 0):
            sid = sr[0]['videoId']
            # log.info(f'songId: {sid}')

            # check if duplicate
            if (sid in plIds):
                log.warning(f"Duplicate id: {sid}:{s}")
            else:
                plIds.append(sid)
    log.debug(f'plIds: {plIds}')
    return plIds


def uploadList(log, ytm, plIds):
    # create a new playlist via list of id's
    plid = ytm.create_playlist('ytmapi test', 'test description')
    log.debug(f'plid: {plid}')

# add songs to playlist
    r = ytm.add_playlist_items(plid, plIds)
    log.info(f"add_playlist status: {r['status']}")
    log.debug(f"add_playlist results: {r}")
    return plid


def uploadOneTime(log, ytm, plIds):
    ''' add song one at a time '''

    plid = ytm.create_playlist('ytmapi test', 'test description')
    log.debug(f'plid: {plid}')
    for z in plIds:
        r = ytm.add_playlist_items(plid, videoIds=[z])
        if (r['status'] != 'STATUS_SUCCEEDED'):
            log.info(f"add_playlist status: {r['status']}")
            log.debug(f"add_playlist results: {r}")


################## main ##################################
log = configLogging()
log.info('START >>>>>>>>>>>>>>>>>>>>>>>>>>>>')
ytm = YTMusic('headers_auth.json')
songs = readSongs(IN_CSV, log)
log.info(f"#songs: {len(songs)}")
# writeCsv(songs)

# combine title & artist, skip first line
songsSearch = []
for i in songs[1:]:
    songsSearch.append(' - '.join(i))
# log.debug(f'songsSearch: {songsSearch}')
log.info(f"search time: {time.time()-start_time}")

# save search data
with open('data/songsSearch.txt', 'w') as fp:
    # fp.write(str(songsSearch))
    fp.write('\n'.join(songsSearch))

plIds = getSongIds(log, ytm, songsSearch)
log.info(f"song id's time: {time.time()-start_time}")

# save plIds
with open('data/plIds.txt', 'w') as fp:
    fp.write('\n'.join(plIds))

# make id's unique
plIds = list(set(plIds))


# uploadOneTime(log, ytm, plIds)
plid = uploadList(log, ytm, plIds)

# END PROGRAM
log.info(f"Done execution time: {time.time()-start_time}")
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

# config log
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# logging.basicConfig()

# print logging tree
# with open('no-cfg.txt', 'a') as fp:
#     fp.write(logging_tree.format.build_description())
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

# write logging cfg tree
# with open('after-cfg.txt', 'a') as fp:
#     fp.write(logging_tree.format.build_description())
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
