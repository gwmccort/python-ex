#!/usr/bin/python3
################################################
# use BeautifulSoup to parse evernote enex file
# TODO: multi page need to be parsed
################################################

import requests
from bs4 import BeautifulSoup

f = open("data/Notebooks - Evernote (1).mhtml")
soup = BeautifulSoup(f, 'lxml')  # TODO: is lxml right?

# verify results
# print(soup.body.prettify())

# find first notbook title
# t = soup.find('span', attrs={'id': '3D"qa-NOTEBOOK_TITLE"'})
# print(t.prettify())
# print('-----------------------')
# print(t.text)

# print all notebook titles TODO: need to decode not finding all
for nb in soup.findAll('span', attrs={'id': '3D"qa-NOTEBOOK_TITLE"'}):
    print(nb.text)
