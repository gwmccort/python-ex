''' ytmusicapi demo '''

# %%
from ytmusicapi import YTMusic

ytm = YTMusic('headers_auth.json')

# %%
''' create a new playlist '''
plName = 'ytmapi test'
plIds = ytm.create_playlist('ytmapi test', 'my description')
plIds

# %%
''' delete playlist by name '''
plName = 'ytmapi test'
plIds = ytm.get_library_playlists()
for pl in plIds:
    # print(f"title: {pl['title']} count: {pl.get('count')}")

    if (pl['title'] == plName):
        print(f"Deleting title: {pl['title']}")
        r = ytm.delete_playlist(pl['playlistId'])
        # print('delete response:', r)
        # print('delete response keys', r.keys())
    else:
        print('Skiping  title:', pl['title'])


# %%
''' delete a playlist '''
sr = ytm.search('ytmapi test',
                filter="playlists",
                limit=5
                )
print('sr len:', len(sr))
for pl in sr:
    # print(type(i))
    # print(i)
    print(pl.get('title'))

# %%
''' search for a song '''
sr = ytm.search('old and in the way')
for pl in sr:
    print(type(pl))

# %%

sr = ytm.search('old and in the way')
sr[0]['artist']
for pl in sr:
    print('-------------------')
    type = pl.get('resultType')
    # print(type)
    # if (type == 'artist'):
    if (type == 'album'):
        artist = pl.get('artist')
        print('type:', type, 'artist:', artist)
    else:
        print(pl)


# %%
''' read artist from playlist '''
plIds = ytm.get_playlist('PLmhv2KJt_0TpRnvgYEEjPNT0JZtzfOFaF')
pl_title = plIds['title']
pl = 0
for t in plIds['tracks']:
    # print('keys:', t.keys())
    print('title:', t['title'])
    # first artist
    artist = t['artists'][0]['name']
    print('artist:', artist)
    # print('title:', t['title'],
    #       'artists:', t['artists'])
    pl += 1
# %%
plIds['tracks'][0]['title']
