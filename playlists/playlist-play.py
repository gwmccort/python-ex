# %%
import playlists.playlist as playlist

# %%
''' read Google Search'''
pl = playlist.GooglePlaylist()
df = pl.read()

# %%
''' read Roots Music Service '''
pl = playlist.RmsPlaylist()
df = pl.read()

# %%
''' update rms_playlist.csv with latest from Roots Music Service (weekly) '''
pl = playlist.RmsPlaylist()
df = pl.read()
pl.merge()
pl.write()

# %%
''' read Bluegrass Today '''
pl = playlist.BgtPlaylist()
df = pl.read()

# %%
''' update bgt_playlists.csv with latest from Bluegrass Today (monthly) '''
pl = playlist.BgtPlaylist()
df = pl.read()
pl.merge()
pl.write()

# %%
