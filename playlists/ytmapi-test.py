# %%
from ytmusicapi import YTMusic

ytm = YTMusic('headers_auth.json')

# api.search('test')
sr = api.search_songs('wild horses - grateful dead')
# print(type(sr))
# print(sr)
# for s in sr['items']:
#     print(type(s))
#     # print(s)
#     print(s['name'])
#     print(s['artists'][0]['name'])
#     print(s['artists'][0]['id'])
#     # print(s.keys())

print(sr['items'][0]['name'])
print(sr['items'][0]['artists'][0]['name'])
for song in sr:
    print(song)
    print(type(song))

# %%

for s in sr['items']:
    print('------------------')
    # print(s)
    print('song name:', s['name'])
    print('artist:', s['artists'][0]['name'])
    print('album:', s['album']['name'])

# %%
fr = sr['items'][0]
print('song:', fr['name'])
print('artist:', fr['artists'][0]['name'])
print('album:', s['album']['name'])


# %%
''' get list of liked songs '''
liked = ytm.get_liked_songs()
# print(liked)
# type(liked)
# liked['tracks'][0]['title']
for t in liked['tracks']:
    print('title:', t['title'])


# %%
