''' download youtube music like songs '''

# %%
import requests
import email
from bs4 import BeautifulSoup

url = "https://music.youtube.com/playlist?list=LM"
page = requests.get(url)

# %%
''' write html to file '''
with open('data/ytm-likes.html', "w") as fp:
    fp.write(page.text)

# %%
''' read saved mhtml file via chrome '''
with open('data/YouTube Music.mhtml') as fp, open('data/ytm-likes.txt', 'w') as ofp:
    msg = email.message_from_file(fp)
    for part in msg.walk():
        if (part.get_content_type() == 'text/html'):
            soup = BeautifulSoup(part.get_payload(decode=True),
                                 features="lxml")
            songs = soup.find_all('div',
                                  {'class': 'flex-columns style-scope ytmusic-responsive-list-item-renderer'})
            for song in songs:
                song_title = song.find('a')
                artist = song_title.find_next('a')
                ofp.write(f'{artist.text} - {song_title.text}\n')
