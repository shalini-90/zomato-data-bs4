import os 
import swig_api 
import requests
import pandas as pd
from bs4 import BeautifulSoup 

pd.set_option('display.max_columns', None)

def createfolder(directory): 
    try: 
        if not os.path.exists(directory): 
            os.makedirs(directory)
            print(f'{directory} created!')
        else:
            print(f'{directory} already exists!') 
    except OSError: 
        print ('Error: Creating directory.' + directory) 

def get_restaurants_links():
    pg_no = 1 
    while True: 
        res = requests.get(f'https://www.swiggy.com/city/indore?page={pg_no}') 
        print(res.status_code)
        if res.status_code != 200 : 
            break 
        content = BeautifulSoup(res.content, 'html.parser')  
        links = content.find_all('a',attrs={"class":"_1j_Yo"}) 
        print(f'\nNo of Restaurants in page no {pg_no}: ', len(links))
        if not links :
            break
        for link in links: 
            restaurant_link = link['href']
            get_restaurant_data(restaurant_link) 
        pg_no+=1 

def data_upload_to_gsheet(data, restaurant_name):
    print('Uploading data to Google Sheet')
    df = pd.DataFrame(data)
    df.insert(0, 'res_name', restaurant_name)
    df.to_csv(f"RESTAURANTS_ORDERS/{restaurant_name}.csv") 
    swig_api.append_googlesheet(df.values.tolist())  
    print('Data Successfully uploaded!')

def get_restaurant_data(restaurant):
    restaurant_name = restaurant.split('/')[-1]
    print('\nGetting Restaurant Data')
    print(f'\n\t Scrapping Menu for :{restaurant_name}\n')

    res = requests.get(f'https://www.swiggy.com{restaurant}') 
    content = BeautifulSoup(res.content, 'html.parser')
    menu_list = content.find_all('div',attrs={"class":"_2wg_t"})
    print('No of items in menu:', len(menu_list)) 
    res_name = content.find('h1', attrs={"class":"_3aqeL"}).text.replace("/",' ') 

    data = []
    for menu in menu_list:  
        desc, dish_name, price, img = '', '', '', ''
        desc = menu.find('div', attrs={"class":"styles_itemDesc__3vhM0"})
        dish_name = menu.find('h3', attrs={"class":"styles_itemNameText__3ZmZZ"}).text
        price = menu.find('span', attrs={"class":"rupee"}).text 
        img = menu.find('img', attrs={"class":"styles_itemImage__3CsDL"})

        print('\nDish Name:', dish_name) 
        print('Price:', price) 
        if desc:
            desc = desc.text
            print('Description:', desc)
        else: print('Description not Found!')
        if img: 
            img = img['src']
            print('Image URL:', img) 
        else: print('No Image Found!') 

        data.append([ dish_name, price, img, desc])

    if not data: 
        return
    data_upload_to_gsheet(data, res_name) 

get_restaurants_links() 
