from selenium import webdriver
import requests
import bs4
from bs4 import BeautifulSoup
import json 
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium
import time
from selenium.webdriver.support.ui import WebDriverWait




driver = webdriver.Chrome('/Users/richeyjay/Downloads/chromedriver')
driver.get('https://finance.yahoo.com/calendar/earnings?from=2020-07-26&to=2020-08-01&day=2020-07-29')

css_selector = "Va(m) H(20px) Bd(0) M(0) P(0) Fz(s) Pstart(10px) O(n):f Fw(500) C($linkColor)"
button_element = driver.switch_to.frame(driver.find_element_by_class_name(css_selector))
WebDriverWait(driver, 10)
button_element.click()
WebDriverWait(driver, 10)
driver.close()