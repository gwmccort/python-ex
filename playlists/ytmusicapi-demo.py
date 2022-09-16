''' ytmusicapi demo '''

# %%
from ytmusicapi import YTMusic

ytm = YTMusic('headers_auth.json')

# %%

sr = ytm.search('old and in the way')
for i in sr:
    print(type(i))

# %%

sr = ytm.search('old and in the way')
sr[0]['artist']
for i in sr:
    print('-------------------')
    type = i.get('resultType')
    # print(type)
    # if (type == 'artist'):
    if (type == 'album'):
        artist = i.get('artist')
        print('type:', type, 'artist:', artist)
    else:
        print(i)


# %%
''' read artist from playlist '''
pl = ytm.get_playlist('PLmhv2KJt_0TpRnvgYEEjPNT0JZtzfOFaF')
pl_title = pl['title']
i = 0
for t in pl['tracks']:
    # print('keys:', t.keys())
    print('title:', t['title'])
    # first artist
    artist = t['artists'][0]['name']
    print('artist:', artist)
    # print('title:', t['title'],
    #       'artists:', t['artists'])
    i += 1
# %%
pl['tracks'][0]['title']
