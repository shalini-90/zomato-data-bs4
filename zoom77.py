from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import os
import pandas as pd 
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

def createFolder(directory): 
    try: 
        if not os.path.exists(directory): 
            os.makedirs(directory) 
    except OSError: 
        print ('Error: Creating directory.' + directory) 


driver.get('https://www.zomato.com/indore') 
time.sleep(4)
driver.maximize_window()
time.sleep(5)  
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
time.sleep(5) 
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)
time.sleep(5)

box=driver.find_elements(By.CLASS_NAME,'sc-rbbb40-0.iwHbVQ') 
box[5].click() 
cc=driver.page_source 

place_links=[]
content = BeautifulSoup(cc, 'html.parser') 
# div link for places 
links=content.find('div',attrs={"class":"sc-bke1zw-0 fIuLDK"}) 
print(links.find_all('href')) 
for ul in links.find_all('div'): 
    a=ul.find('a')
    if a: 
       place_links.append(a['href']) 
print(place_links) 

def get_restaurants_links(content):
   
    links1=content.find_all('a',attrs={"class":"sc-fgrSAo ctkAaV"})

    restaurant_links = []
    print(f'\nREstaurants_link:',len(links1)) 
 
    for li in links1: 
        restaurant_link=li['href'] 
        print(restaurant_link)
        restaurant_links.append(restaurant_link)
        get_restaurant_data(restaurant_link)

def get_restaurant_data(restaurant_link):
    driver.get(f'https://www.zomato.com{restaurant_link}')
    # time.sleep(5)
    ps = driver.page_source
    content = BeautifulSoup(ps, 'html.parser') 
    dish_name_list=[]
    dish_price_li=[] 
    dish_description_list=[] 
     
    res_name=content.find('h1', attrs={"class":"sc-7kepeu-0 sc-eilVRo eAhpQG"}).text
    # res_name.text
    print(res_name) 

    menuss=content.find_all('div',attrs={"class":"sc-1s0saks-13 kQHKsO"})  
    # for idx, menu in enumerate(menuss):
    for menu in menuss:
        menu_name=menu.find('h4', attrs={"class":"sc-1s0saks-15 iSmBPS"}).text
        dish_name_list.append(menu_name)
        print(menu_name) 
        menu_price=menu.find('span', attrs={"class":"sc-17hyc2s-1 cCiQWA"}).text 
        dish_price_li.append(menu_price)  
        print(menu_price) 
    

    try: 
        menu_description=content.find('p', attrs={"class":"sc-1s0saks-12 hcROsL"}).text 
        dish_description_list.append(menu_description)
        print(menu_description) 

    except: 
        dish_description_list.append(None)
        print(None) 
    get_csv(dish_name_list,  dish_price_li, dish_description_list, res_name ) 

createFolder('./RESTAURANTS/')   



def get_csv(dish_name_list, dish_price_li, dish_description_list, res_name):
    order={   
    
    "DISH": dish_name_list, 
    "PRICE":dish_price_li, 
    "DESC" :dish_description_list,
    
    }  
    if not order : 
        return  
    # print('********', zoo)
    df = pd.DataFrame.from_dict(order, orient='index')
    df = df.transpose()

    df.to_csv(f"RESTAURANTS/{res_name}.csv") 


for link in place_links :
# r=requests.get(link)
# print(r.status_code) 
    page = driver.get(link) 
    content = BeautifulSoup(cc, 'html.parser')   
    get_restaurants_links(content) 
 





   
    







 
 
 
 
 # try:
    #     menu_rating=menu.find('span', attrs={"class":"sc-z30xqq-4 hTgtKb"})
    #     print(menu_rating.text) 
    # except: 
    #     print(None) 

# content = BeautifulSoup(res.content, 'html.parser')  
#         links = content.find_all('a',attrs={"class":"_1j_Yo"}) 
#         print(f'\nNo of Restaurants in page no {pg_no}: ', len(links))
#         if not links :
#             break
#         for link in links: 
#             restaurant_link = link['href']
# for i in links1.find_all('a'): 
#     aa=i.find('a')
     




