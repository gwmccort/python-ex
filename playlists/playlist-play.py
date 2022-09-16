# %%
import Playlist

# %%
''' read Google Search'''
pl = Playlist.GooglePlaylist()
df = pl.read()

# %%
''' read Roots Music Service '''
pl = Playlist.RmsPlaylist()
df = pl.read()

# %%
''' update rms_playlist.csv with latest from Roots Music Service (weekly) '''
pl = Playlist.RmsPlaylist()
df = pl.read()
pl.merge()
pl.write()

# %%
''' read Bluegrass Today '''
pl = Playlist.BgtPlaylist()
df = pl.read()

# %%
''' update bgt_playlists.csv with latest from Bluegrass Today (monthly) '''
pl = Playlist.BgtPlaylist()
df = pl.read()
pl.merge()
pl.write()

# %%
