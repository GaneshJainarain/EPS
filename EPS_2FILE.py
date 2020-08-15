import requests
import bs4
from bs4 import BeautifulSoup
from time import sleep
import json 
import pandas as pd 
import numpy
from datetime import datetime




def main():
    program = EPS_2FILE('2020-08-14')
    #program.validate_date()
    program.val
    print(program.val)

    print("========================================================")
    print("========================================================")
    print(program.url)

    print("========================================================")
    print("========================================================")
    print(program.url2)

    print("========================================================")
    print("========================================================")
    print(program.r)

    print("========================================================")
    print("========================================================")
    print(program.Company_Name_List)
    print("========================================================")
    print("========================================================")

    print(program.Create_Matrix)
    print("========================================================")
    print("========================================================")
    print(program.rows)

    print("========================================================")
    print("========================================================")
    print(program.Company_Name())
    print("========================================================")
    print("========================================================")
    print(program.Create_Matrix())
    print("========================================================")
    print("========================================================")
    print(program.validate_date())



class EPS_2FILE:
    
    #val = input("Enter date in YYYY-MM-DD Format:")

    def __init__(self, val):
        self.url = 'https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day='
        self.val = input("Enter date in YYYY-MM-DD Format:")
        self.url2 = self.url + self.val
        self.r = requests.get(self.url2)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        self.rows = self.soup.select('tbody tr td')
        self.rows2 = self.soup.select('tbody tr')

        self.row = self.rows[0]
        self.row2 = self.rows2[0]
        self.Company_Name_List = self.soup.find_all("td", class_ = "Va(m) Ta(start) Pend(10px) Pstart(6px) Fz(s)")


    def validate_date(self):
        try:
            if len(self.val) == 10: 
                datetime.strptime(self.val, '%Y/%m/%d')
                return "NICE"
            else: 
                return False

        except ValueError:
            return "ERRORR"
    
    def Company_Name(self):
        for Company in self.Company_Name_List:
            print(Company.text)

    def Create_Matrix(self):

        n = 6
        m = int(len(self.rows)/6)
        #print(m*n)
        a = [[0 for x in range(n)] for x in range(m)] 
        #print(a) 
        new = []
        for i in self.rows:
            l = new.append(i.text)
        composite_list = [new[x:x+6] for x in range(0, len(new),6)]

        h1 = self.soup.find("h3", class_ = "Mb(10px) D(ib) Mend(25px)").text
        h2 = self.soup.find('span',class_ = 'Mstart(15px) Fw(500) Fz(s)').text
        Date = h1.replace(h2, '')

        print(Date)
        print("SYMBOL||  COMPANY||  EARNINGS CALL TIME||  EPS EST||  REPORTED EPS||  SURPRISE% ")

        outF = open("data.txt", "w")
        outF.write(Date)
        outF.write('\n')

        for everyi, self.row2 in zip(composite_list,self.rows2):
            x = 'https://finance.yahoo.com' + self.row2.select_one('.C\\(\\$linkColor\\)')['href']
            print(everyi)
            print(x)
            outF.write("SYMBOL||  COMPANY||  EARNINGS CALL TIME||  EPS EST||  REPORTED EPS||  SURPRISE% ")
            outF.write(str(everyi))
            outF.write('\n')
            outF.write('\n')
            outF.write("LINK:" + " " + x)
            outF.write('\n')
            outF.write('\n')

        outF.close()


main()
