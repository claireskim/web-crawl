# Scrapes the front page of nytimes.com for the headlines
# JS version coming

import requests
from bs4 import BeautifulSoup
 
url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text)
headings = []

title = soup.find_all('h2',{'class':['css-1qwxefa','css-n2blzn']})

for row in title:
     headings.append(row.text)

print(headings)
