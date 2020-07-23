import requests
from bs4 import BeautifulSoup
from time import sleep
import json 
import pandas as pd 

url = 'https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day=2020-07-20'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr')
row = rows[0]

name = row.select_one('.C($linkColor)').text.strip()
print(name)


print("==============================================")
yahoo_page = row.select_one('.C($linkColor)')['href']
yahoo_page = 'https://finance.yahoo.com' + yahoo_page
print(yahoo_page)
print("==============================================")



print("==========================================")

pages =  ['https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day=2020-07-20',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-07-21',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-07-22',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-07-23',
          'https://finance.yahoo.com/calendar/earnings?from=2020-07-19&to=2020-07-25&day=2020-07-24'

          
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
