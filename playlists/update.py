''' update playlist csv files '''

import playlists.playlist as playlist
import argparse


def parse_args():
    # use group to require one of several parameters
    # https://www.anycodings.com/1questions/5041530/python-argparse-make-at-least-one-argument-required

    parser = argparse.ArgumentParser(
        description='update playlist csv from websites')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--all',
                       action='store_true',
                       help='update all playlists')
    group.add_argument('-r', '--rms',
                       action='store_true',
                       help='update Roots Music Service playlist')
    group.add_argument('-b', '--bgt',
                       action='store_true',
                       help='update Bluegrass Today playlist')
    return parser.parse_args()


def main():
    args = parse_args()

    if (args.all):
        for pl in [playlist.RmsPlaylist(), playlist.BgtPlaylist()]:
            pl.read()
            pl.merge()
            pl.write()
    else:
        if (args.rms):
            pl = playlist.RmsPlaylist()
        elif (args.bgt):
            pl = playlist.BgtPlaylist()
        pl.read()
        pl.merge()
        pl.write()


if __name__ == "__main__":
    main()
