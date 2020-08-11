import requests
from bs4 import BeautifulSoup
from time import sleep
import json 
import pandas as pd 

url = 'https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day=2020-08-06'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')
row = rows[0]

#name = row.select_one('C(linkColor)').text.strip()
#print(name)
print("==========================================")
pages =  ['https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day=2020-08-03',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-08-04',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-08-05',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-08-06',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-08-07'

          
          ]

data = []
for page in pages:
    G = requests.get(page)
    soup = BeautifulSoup(G.content, 'html.parser')
    rows = soup.select('tbody tr')
    print(page)

    for row in rows:
        
        d = dict()

        #d['Day Header'] = Day_Header
        #d['Stock Name'] = 
        d['Ticker Symbol'] = row.select_one('.C($linkColor)').text.strip()
        d['Stock Link'] = 'https://finance.yahoo.com' + row.select_one('.C($linkColor)')['href']
        

        data.append(d)

        with open('yahoo_page_finance.json', 'w') as f:
            json.dump(data, f)

        with open('yahoo_page_finance.json', 'r') as f:
            data = json.load(f)

#print(data)
print("===========================================")
#print(rows)
