''' read playlist from apple music web site - IN PROGRESS'''
# %%
import email
from bs4 import BeautifulSoup


IN_FILE = 'data/_Jam Band Essentials on Apple Music.mhtml'

with open(IN_FILE) as f:
    message = email.message_from_file(f)
    i = 0
    for part in message.walk():
        i += 1
        if (part.get_content_type() == "text/html"):
            # print(f'part text/html, i: {i}')
            soup = BeautifulSoup(part.get_payload(
                decode=True), features="lxml")

            mydivs = soup.find_all(
                "div", {"class": "songs-list-row__song-name-wrapper"})

            # mydivs = soup.find_all(
            #     "div", {"class": "songs-list-row__song-name"})

            for div in mydivs:
                print(f'song: {div.text.strip()}')
                print(
                    f"artist: {div.find('a', {'class': 'songs-list-row__link'}).text}")

            # ofn = f'{i}apple.html'
            # with open(ofn, 'w') as of:
            #     of.write(soup.prettify())


'''
<div class="songs-list-row__song-name-wrapper">
              <div aria-checked="false" class="songs-list-row__song-name" dir="auto" role="checkbox" tabindex="-1">
               Sahib Teri Bandi - Maki Madni
              </div>
              <div class="songs-list-row__by-line" dir="auto">
               <span>
                <a class="songs-list-row__link" dir="auto" href="https://music.apple.com/us/artist/the-derek-trucks-band/635011" tabindex="-1">
                 The Derek Trucks Band
                </a>
               </span>
              </div>
             </div>
'''
