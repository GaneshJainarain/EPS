import requests
from bs4 import BeautifulSoup
from time import sleep
import json 
import pandas as pd 

url = 'https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day=2020-07-20'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr td')
row = rows[0]
name = row.select_one('.C($linkColor)').text.strip()


Company_Name_List = soup.find_all("td", class_ = "Va(m) Ta(start) Pend(10px) Pstart(6px) Fz(s)")
def Company_Name(Company_Name_List):
    for Company in Company_Name_List:
        return(Company)

X = Company_Name(Company_Name_List)
#print(Company_Name_List)
#print(row.Company_Name_List)
print(rows[0].text)

#print(rows)


for i in rows:
    print(i.text)


