''' Music Grotto 25 Best Bluegras '''

# %%
import requests
from html.parser import HTMLParser
import re

# %%


class MusicGrottoParser(HTMLParser):

    inH2 = False

    def handle_starttag(self, tag: str, attrs):
        # return super().handle_starttag(tag, attrs)
        if tag == 'h2':
            # print('in h2:')
            self.inH2 = True
        else:
            # print('not in h2:')
            self.inH2 = False

    def handle_data(self, data: str) -> None:
        if self.inH2 == True and not data.isspace():

            # use unicode for - char
            rex = r"^(\d+)\) (.*) \u2013 (.*)"
            m = re.search(rex, data)
            if m != None:
                # print(m.groups())
                song = m.group(2)
                artist = m.group(3)
                print(f"{artist} - {song}")


URL = 'https://www.musicgrotto.com/best-bluegrass-songs'
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
req = requests.get(URL, headers=header)
req.status_code
parser = MusicGrottoParser()
parser.feed(req.text)

# %%
