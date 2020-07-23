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



results = soup.find("h3", class_ = "Mb(10px) D(ib) Mend(25px)").text
print(results)
results_fix = soup.find('span',class_ = 'Mstart(15px) Fw(500) Fz(s)').text
print(results_fix)


def results_fix1(results, results_fix):
    x = results.replace(results_fix, '')
    return (x)

results_fix1(results, results_fix)

Day_Header = results_fix1(results, results_fix)
print(Day_Header)