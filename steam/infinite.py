
import shutil
import ntpath
import os.path
from decimal import *
import os
from bs4 import BeautifulSoup
from django.shortcuts import render
import selenium
from selenium import webdriver
import json
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
import time
import requests

requests.packages.urllib3.disable_warnings()

browser = webdriver.Chrome(executable_path='C:/FYP/chromedriver.exe')

browser.get("https://store.ubi.com/sea/all-games?lang=en_SG")
time.sleep(1)
browser.maximize_window()
elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1


game = browser.find_element_by_class_name("samples")
post_elems = game.find_elements_by_xpath("//div[@class='product-tile card    full-tile-link']/a[@href]")

for post in post_elems:
    link =  (post.get_attribute("href"))
    
    
    session = requests.Session()
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = link

    content = session.get(url, verify=False).content
    soup = BeautifulSoup(content, "html.parser")
    try:
        title=soup.find('span',{'class':'breadcrumb-element breadcrumb-element-visible'})
        newtitle=(title.text.strip())
        
        price = soup.find('span',{'class':'price-sales standard-price'}).text
        newprice = price.strip()
        finalprice = (Decimal(newprice.strip('RM')))
        tag = soup.find_all('li',{'class':'product-details-info-item'})[3]
        newtag=(tag.text.strip())
        image =soup.find('img', {'class':['lazyload','swapped','lazy-loaded']})['data-desktop-src']
        
        media_root = '/FYP/django/rise/media'
        if not image.startswith(("data:image", "javascript")):
            #local_filename = image.split('/')[-1].split("?")[0]
            local_filename = newtitle+'.jpg'
            r = session.get(image, stream=True, verify=False)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)

            current_image_absolute_path = os.path.abspath(local_filename)
            shutil.move(current_image_absolute_path, media_root)
    except:
        pass
    

    




image = soup.find('a',{'class':['img-thumb','img-center']})