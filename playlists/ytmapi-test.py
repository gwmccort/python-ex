''' test of ytmusicapi '''
# %%
import logging as log
import pprint
from ytmusicapi import YTMusic

ytm = YTMusic('headers_auth.json')


# %%

log.basicConfig(level=log.INFO)
log.info('Starting>>>>>>>>>>>>')

# pp = pprint.PrettyPrinter()
# pp.pprint(ytm)

r = ytm.search('x', filter='songs')
r

# %%
''' search for song '''
results = ytm.search('old and in way - wild horses',
                     filter='songs')
# print(pp.pprint(results))

# print first results
print('title:', results[0]['title'])
print('id:', results[0]['videoId'])
print('artist:', results[0]['artists'][0]['name'])

# %%


# api.search('test')
# sr = ytm.search_songs('wild horses - grateful dead')
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
