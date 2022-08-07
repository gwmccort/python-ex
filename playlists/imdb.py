# %%
''' get imdb data & process with bs from [ TutPig.com ] Skillshare - Web Scraping Essentials with Python_ Requests and BeautifulSoup '''
import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = 'https://www.imdb.com/search/title/?release_date=2021-01-01,2022-08-7&sort=num_votes,desc&ref=adv_prv'
url = 'https://www.imdb.com/search/title?release_date=2021-01-01,2022-08-7&sort=num_votes,desc&ref_=adv_prv'
page = requests.get(url)
# print(page.ok)

soup = BeautifulSoup(page.content, 'html.parser')

# %%
''' get data from page '''
content = soup.find_all('div', class_='lister-item-content')
movies = list()
for item in content:
    name = item.h3.a.text
    rating = item.strong.text
    # print(f'name:{name} rating:{rating}')
    movies.append((name, rating))

# %%
''' save to csv file'''
df = pd.DataFrame(movies, columns=['Name', 'Ratings'])
df.to_csv('data/imdb.csv')
