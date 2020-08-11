import requests
import bs4
from bs4 import BeautifulSoup
from time import sleep
import json 
import pandas as pd 
import numpy

url = 'https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day='

val = input("Enter date in YYYY-MM-DD Format:")

url = url + val
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
rows = soup.select('tbody tr td')
row = rows[0]
#name = row.select_one('.C($linkColor)').text.strip()


Company_Name_List = soup.find_all("td", class_ = "Va(m) Ta(start) Pend(10px) Pstart(6px) Fz(s)")
def Company_Name(Company_Name_List):
    for Company in Company_Name_List:
        return(Company)

X = Company_Name(Company_Name_List)
#print(Company_Name_List)
#print(row.Company_Name_List)
print(rows[0].text)

#print(rows)
'''
print(len(rows))
for i in rows:
    print(i.text)

type(rows)
'''
n = 6
m = int(len(rows)/6)
print(m*n)
#print(n * m)
a = [[0 for x in range(n)] for x in range(m)] 
#print(a) 
new = []
for i in rows:
    l = new.append(i.text)



print("========================================")
print("========================================")
print("========================================")
print("========================================")
composite_list = [new[x:x+6] for x in range(0, len(new),6)]
print("compo", composite_list)

print("========================================")
print("========================================")
print("========================================")
print("SYMBOL|| COMPANY|| EARNINGS CALL TIME|| EPS EST|| REPORTED EPS|| SURPRISE% ")

outF = open("data.txt", "w")
outF.write("hello")

for everyi in composite_list:
    data = []
    d = dict()
    #print("SYMBOL|| COMPANY    || EARNINGS CALL TIME||   EPS EST|| REPORTED EPS|| SURPRISE% ")
    print(everyi)
    outF.write(str(everyi))
    outF.write('\n')
outF.close()
    

'''
    #print(everyi[0])
    #print(everyi[1])
    #print(everyi[2])
    #print(everyi[3])
    #print(everyi[4])
    #print(everyi[5])

    d['Ticker Symbol'] = everyi[0]
    d['Stock Name'] = everyi[1]
    d['Earnings Call Time'] = everyi[2]
    d['EPS Estimate'] = everyi[3]
    d['Reported EPS'] = everyi[4]
    d['Surprise(%)'] = everyi[5]
    data.append(d)
    print(d.get("Ticker Symbol"))
    print(d.get("Stock Name"))
    print(d.get("Earnings Call Time"))
    print(d.get("EPS Estimate"))
    print(d.get("Reported EPS"))
    print(d.get("Surprise(%)"))
    

print("========================================")
print("========================================")
print("========================================")
print("========================================")

'''

print(composite_list[0][0])
print("=================================================================")

'''
for stock_list in composite_list:
    print(stock_list)
    for sub_list in stock_list:
        print(sub_list)


data = []
for i in composite_list:
    #print(i)
    #print(i[0])
    #print(i[1])
    #print(i[2])
    #print(i[3])
    #print(stock_list[a])
    #print(stock_list[b])
    #print(stock_list[c])
    #print(stock_list[d])
    
    d = dict()

    d['Ticker Symbol'] = i[0]
    d['Stock Name'] = i[1]
    d['Earnings Call Time'] = i[2]
    d['EPS Estimate'] = i[3]
    d['Reported EPS'] = i[4]
    d['Surprise(%)'] = i[5]
    


    #print(stock_list[b]+ "++++++++++++++++++++++++++++++++")
    

    data.append(d)
    print(data)


    with open('yahoo_page_finance.json', 'w') as f:
        json.dump(data, f)

    with open('yahoo_page_finance.json', 'r') as f:
        data = json.load(f)

        

print("==================================================================")
print("==================================================================")
print("==================================================================")
'''
for key, value in d.items():
    print (key, value)

    #print(len(stock_list))

