import requests
import bs4
from bs4 import BeautifulSoup
import json 
from datetime import datetime



#Purpose of the Program:

''' 
I wanted to create a tool for programmers and anyone who was interested in stocks-
to easily pull data simply by running this script and entering input. 
This program is a great way for people to observe the scheduled- 
Earnings Per Share Reports for a specific date. 
Ultimately this program should be used as a tool to enhance-
the user’s trading strategies when planning on making trades when earnings season is on. 
'''


#Main method used to establish the class for running the program
#Calls various other methods used to execute the correct ouput


def main():
    program = EPS_2FILE()
    
    program.validate_date()
    
    print(program.val)

    print("========================================================")
    print("========================================================")
    print(program.url2)

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
    
    #Initializer to establish variables to later be used in other methods 
    #This contains the link im scraping from and the beautifulsoup parser for scraping certain data
    #Error catching is also evident by the try and except blocks 

    def __init__(self):
        self.url = 'https://finance.yahoo.com/calendar/earnings?from=2020-07-12&to=2020-07-18&day='
        
        while True:
            try:
                self.val = input("Enter date in YYYY-MM-DD Format:")
                if len(self.val) == 10: 
                    datetime.strptime(self.val, '%Y-%m-%d')
                break
            except ValueError:
                print("1Oops! The format in which you entered is invalid. Try again using this Format YYYY-MM-DD")

        self.url2 = self.url + self.val
        self.r = requests.get(self.url2)
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        self.rows = self.soup.select('tbody tr td')
        self.rows2 = self.soup.select('tbody tr')

        while True:
            try:
                self.row = self.rows[0]
                self.row2 = self.rows2[0]
                break
            except IndexError:
                print("2Oops! Looks like the date you entered has no Earnings announcements scheduled or you entered an invalid input")
                main()
                break
        self.Company_Name_List = self.soup.find_all("td", class_ = "Va(m) Ta(start) Pend(10px) Pstart(6px) Fz(s)")

    #This method checks to see if the user's input is of the format required 

    def validate_date(self):

        try:
            if len(self.val) == 10: 
                datetime.strptime(self.val, '%Y-%m-%d')
                return "Input is Valid"
            else: 
                return("Please Enter a Valid Date")
                

        except ValueError:
            return "ERRORR"
    
    #This method checks to see if the list Company_Name_List is populated with various companies
    #If there are no Companies announcing Earnings this day the method will return a message stating so
    #If there are companies the method will iterate through the list printing each one 

    def Company_Name(self):

        if self.Company_Name_List == []:
            print("There are no Companies announcing today")
        else:
            for Company in self.Company_Name_List:
                print(Company.text)

    #This method is responsible for creating the matrix display in the data.txt file

    def Create_Matrix(self):

        #Creates the New list, and makes 6 columns for the 6 distinctive columns of data 

        new = []
        for i in self.rows:
            new.append(i.text)
        composite_list = [new[x:x+6] for x in range(0, len(new),6)]

        #h1 and h2 are responsible for displaying the earnings date and the amount of companies announcing

        while True:
            try:
                h1 = self.soup.find("h3", class_ = "Mb(10px) D(ib) Mend(25px)").text
                h2 = self.soup.find('span',class_ = 'Mstart(15px) Fw(500) Fz(s)').text


                Date = h1.replace(h2, '')
                Number_of_companies = (h2.replace(h1, ""))
                print(Date)
                
                print("SYMBOL| COMPANY  |  EARNINGS CALL TIME |  EPS EST |  REPORTED EPS|  SURPRISE% ")

                #Creates a new file called data.txt and opens it for writing
                #Writes the Date and # of Companies announcing that day 

                outF = open("data.txt", "w")
                outF.write("                                " + Date)
                outF.write('\n')
                outF.write("                                   " + Number_of_companies)
                outF.write('\n')
                outF.write('\n')

                #This loop is responsible for unpacking and looping through two lists at a time
                #Every company is associated with data and each company is in its own array in a multidimensional array
                #loop through this multidimensional array then wrote each one in the data.txt file
                #The other loop loops through the associated link list for the corresponding company 
                #Writes the link associated with the company under the array

                for everyi, self.row2 in zip(composite_list,self.rows2):
                    x = 'https://finance.yahoo.com' + self.row2.select_one('.C\\(\\$linkColor\\)')['href']
                    print(everyi)
                    print(x)
                    outF.write("SYMBOL||  COMPANY||  EARNINGS CALL TIME||  EPS EST||  REPORTED EPS||  SURPRISE% ")
                    outF.write('\n')
                    outF.write(str(everyi))
                    outF.write('\n')
                    outF.write('\n')
                    outF.write("LINK:" + " " + x)
                    outF.write('\n')
                    outF.write('\n')

                outF.close()
    
                break
            #Catches any AttributeError 
            except AttributeError:
                print("3Oops! Looks like the date you entered has no Earnings announcements scheduled")
                main()
                break
            


main()
