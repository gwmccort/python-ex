''' ytm library demo '''

# %%
import ytm

api = ytm.YouTubeMusic()
api

# %%
album = api.album('MPREb_ctJ5HEJw8pg')
album

# %%

pl = api.playlist('PLmhv2KJt_0Tr5JGDzXTcHI1w294oAHyf2')
# list(pl)

for track in pl['tracks'][:5]:  # First 5 Tracks
    print(track['artist']['name'], '-', track['name'])


# %%
''' find song from search '''
api.search_songs('wild horses')


# %%

api.search('hello')
# %%
