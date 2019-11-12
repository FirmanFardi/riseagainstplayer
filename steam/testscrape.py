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


def epic():
    
        
    session = requests.Session()
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://www.humblebundle.com/store/search?sort=bestselling&hmb_source=store_navbar'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")

    
    game = soup.find_all('a',{'class':'entity-link'}) 

    for i in game:
        print(i)





epic()
        