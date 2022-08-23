

# %%
# import requests
import datetime
import pandas as pd
from bs4 import BeautifulSoup


class PocketBookmark:

    POCKET_EXPORT = 'data/ril_export.html'
    bookmarks = list()

    @staticmethod
    def read():
        with open(PocketBookmark.POCKET_EXPORT) as f:
            html = f.read()
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find_all('li')
            tags = list()
            for i in items:
                a = i.find('a')
                link = a['href']
                date = a['time_added']
                title = a.text
                for t in a['tags'].split(','):
                    tags.append(t)

                bm = PocketBookmark(link, title, date, tags)
                PocketBookmark.bookmarks.append(bm)

    def __init__(self, link, title, date, tags) -> None:
        self.tags = tags
        self.link = link
        self.title = title
        self.date = date
        # self.date = datetime.datetime.fromtimestamp(date)


# %%
with open(PocketBookmark.POCKET_EXPORT) as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

# %%
titles = list()
links = list()
dates = list()
tags = set()
items = soup.find_all('li')
for i in items:
    a = i.find('a')
    titles.append(a.text)
    links.append(a['href'])
    dates.append(a['time_added'])
    for t in a['tags'].split(','):
        tags.add(t)


# %%
def read():
    print('in read')
    pass


def main():
    PocketBookmark.read()
    for i in PocketBookmark.bookmarks:
        print('----------------------')
        print(f'title: {i.title}')
        print(f'url: {i.link}')
        print(f'date: {i.date}')
        print(f'tags: {i.tags}')


if __name__ == "__main__":
    main()

# %%
