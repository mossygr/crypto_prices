from re import X
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from termcolor import colored

url = "https://www.tradingview.com/symbols/BTCUSDT/"

options = Options()
options.headless = True

driver = webdriver.Chrome(".\chromedriver.exe", options=options)# MS WINDOWS
driver.get(url)

while(True):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', {"class" : "js-symbol-last"}).text  
    print (colored(temp,'red'))
    time.sleep(1)

driver.close()