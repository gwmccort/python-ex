#!/usr/bin/python3
########################################
# bs.py - parse html with beautifulsoup
#
# from: https://opensource.com/article/21/9/web-scraping-python-beautiful-soup
########################################

import requests

url = 'https://notes.ayushsharma.in/technology'

data = requests.get(url)

print(data.text)
