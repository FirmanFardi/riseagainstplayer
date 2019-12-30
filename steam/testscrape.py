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


def steam():
    
    pages = [2]
    
    for page in pages:
        session = requests.Session()
        session.headers = {
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
        url = 'https://store.steampowered.com/search/?page='+format(page)+'&tags=19'

        content = session.get(url, verify=False).content
    
        soup = BeautifulSoup(content, "html.parser")
        topseller = soup.find('div', {'id': 'search_resultsRows'})
        steam = topseller.find_all('a') 
        
        for i in steam:
            link=i['href']
            print(link)
            
            session = requests.Session()
            session.headers = {
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
            url = link
            content = session.get(url, verify=False).content

            soup = BeautifulSoup(content, "html.parser")
            
            try:
                metascore = soup.find('meta', {'itemprop': 'ratingValue'})['content']
                print(metascore)
                title = soup.find('div',{'class':'apphub_AppName'}).text
                print(title)
                genre = soup.find('div',{'class':'details_block'}).a.text
                print(genre)
                developer = soup.find('div',{'class':'dev_row'}).a.text
                print(developer)

                tags = soup.find_all('a',{'class':'app_tag'})
                for i in tags:
                    tag=i.text.strip()
                    print(tag)
            except:
                pass

steam()