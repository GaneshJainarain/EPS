from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time



driver = webdriver.Chrome('/Users/richeyjay/Desktop/EPS1/chromedriver')
driver.get("https://finance.yahoo.com/calendar/earnings?from=2020-07-26&to=2020-08-01&day=2020-07-28")

while True:
    try:
        time.sleep(7)
        checkbox = driver.find_element_by_xpath('//*[@id="cal-res-table"]/div[2]/button[3]')
        
        checkbox.click()
        time.sleep(7)
        print('yes1!')

        checkbox2 = driver.find_element_by_xpath('//*[@id="cal-res-table"]/div[2]/button[3]')
        checkbox2.click()
        time.sleep(7)
        print('yes2!')

        checkbox3 = driver.find_element_by_xpath('//*[@id="cal-res-table"]/div[2]/button[3]')
        checkbox3.click()
        time.sleep(7)
        print('yes3!')
        
    except selenium.common.exceptions.NoSuchElementException:
        print("end1")
        break
    except selenium.common.exceptions.ElementClickInterceptedException:
        print('end2')
        break
     

driver.close()









