import requests
from bs4 import BeautifulSoup
from time import sleep
import json 
import pandas as pd 

url = "https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day=2020-08-06"

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
    h1 = soup.find("h3", class_ = "Mb(10px) D(ib) Mend(25px)").text
    h2 = soup.find('span',class_ = 'Mstart(15px) Fw(500) Fz(s)').text
    Day_Header = h1.replace(h2, '')
    Company_Name_List = soup.find_all("td", class_ = "Va(m) Ta(start) Pend(10px) Pstart(6px) Fz(s)")



    for row in rows:
        
        d = dict()

        d['Day Header'] = Day_Header
        #d['Stock Name'] = Company_Name_List
        d['Ticker Symbol'] = row.select_one('.C\\(\\$linkColor\\)').text.strip()
        d['Stock Link'] = 'https://finance.yahoo.com' + row.select_one('.C\\(\\$linkColor\\)')['href']
    

        data.append(d)

        with open('DATA.json', 'w') as f:
            json.dump(data, f)

        with open('DATA.json', 'r') as f:
            data = json.load(f)
    print("===========================================")


print(data)
print("===========================================")
#print(rows)
