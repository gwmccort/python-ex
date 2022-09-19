''' app that uses Playlist class '''

import playlist
import logging


def configLogs():
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
    # fh.setFormatter(formatter)

    log.addHandler(ch)
    log.addHandler(fh)
    return log


if (__name__ == "__main__"):
    log = configLogs()


log = logging.getLogger(__name__)
logging.basicConfig(
    filename='playlist-app.log',
    level='INFO'
    # level='DEBUG'
)
log.info('Starting >>>>>')

pl = playlist.RmsPlaylist()
pl.read()

pl.ytmUpload()


log.info('End')
