# Scrape the front page of NY Times for the headlines
# Uses BeautifulSoup
# JS version coming

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text)
headings = []

title = soup.findAll('h2', {'class': 'css-1qwxefa'})

for row in title:
     headings.append(row.text)

print(headings)
