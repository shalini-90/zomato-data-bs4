from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#import pandas as pd 
import csv
import zo66_api
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 

import gspread

from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials 
from bs4 import BeautifulSoup



import requests
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
options = Options() 

import urllib.request as r

# options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get('https://www.zomato.com/indore/shree-sai-dosa-bhavan-3-vijay-nagar/order') 
            
time.sleep(4)
driver.maximize_window()
driver.delete_all_cookies()
driver.refresh()
time.sleep(5) 
cc=driver.page_source 

place_links=[]
content = BeautifulSoup(cc, 'html.parser')  

with open('pg.txt', 'w') as f:
    f.write(cc)

res_name=content.find('h1', attrs={"class":"sc-7kepeu-0 sc-eilVRo eAhpQG"}).text 
print(res_name) 
# menu_list=content.find_all('div',attrs={"class":"sc-fXchrD famuTZ"})
# sections = content.find_all('section', attrs={"class":"sc-fXUpvm kWsZnV"})
# if not sections:
#     sections = content.find_all('section', attrs={"class":"sc-hnQkKq eAyhHf"})

# print(sections) 

menuss=content.find_all('div',attrs={"class":"sc-1s0saks-13 kQHKsO"})  
for menu in menuss:
    menu_name=menu.find('h4', attrs={"class":"sc-1s0saks-15 iSmBPS"}).text
    print(menu_name) 
    menu_price=menu.find('span', attrs={"class":"sc-17hyc2s-1 cCiQWA"}).text  
    print(menu_price) 
    try:
        menu_rating=menu.find('span', attrs={"class":"sc-z30xqq-4 hTgtKb"})
        print(menu_rating.text) 
    except: 
        print(None) 

    try: 
        menu_description=content.find('p', attrs={"class":"sc-1s0saks-12 hcROsL"}).text 
        print(menu_description) 

    except: 
        print(None) 
    img_div = content.find_all('div', attrs={"class":"sc-s1isp7-1 kmRBaC sc-1s0saks-16 dfjlEy"})
    print(img_div)
    for div in img_div:
        img = div.find('img') 
        if img: 
            print('img:', img)
            img = img['src']
            print('Image URL:', img) 

            # driver.close() 
# for ul in soup.find_all('ul', class_='listing'):
# ...     for li in ul.find_all('li'):
# ...         a = li.find('a')
# ...         print(a['href'], a.get_text()) 

 # print('\n======',a)
        # print('\n+++++++',a['href']) 


# menu_list=content.find_all('div',attrs={"class":"sc-gsVOdK KIrAb"})
# # sc-gsVOdK KIrAb
# print(menu_list, ' -----')
# for menu in menu_list:
#     menu_name=menu.find('h4', attrs={"class":"sc-1s0saks-15 iSmBPS"}).text
#     print(menu_name) 
#     menu_price=menu.find('span', attrs={"class":"sc-17hyc2s-1 cCiQWA"}).text 
#     print(menu_price)  
#     menu_rating=menu.find('span', attrs={"class":"sc-z30xqq-4 hTgtKb"}).text 
#     print(menu_rating) 


   
