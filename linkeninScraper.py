from string import capwords
import requests # http requests
from bs4 import BeautifulSoup # Webscrape
from collections import defaultdict # Default dictionary: store a list with each key
import pandas as pd     # DF


def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    url= f'https://www.linkedin.com/jobs/jobs-in-miami-fl?trk=homepage-basic_intent-module-jobs&position=1&pageNum={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div',class_ = 'base-card')
    for item in divs:
            title = item.find('a').text.strip()
            company = item.find('h4', class_= 'base-search-card__subtitle').text.strip()
            position = item.find('h3', class_ = 'base-search-card__title').text.strip().replace('/n','')

            job = {
                'title': title,
                'company': company,
                'position': position,
            }
            joblist.append(job)
    return

joblist = []

for i in range(0,40,10):
    print(f'Getting page, {i}')
    c = extract(0)
    transform(c)

df = pd.DataFrame(joblist) 
print(df.head())
df.to_csv('jobs.csv')