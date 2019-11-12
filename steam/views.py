from .models import Steam
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


"""
def gog():

    session = requests.Session()
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://www.epicgames.com/store/en-US/'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")

    epic = soup.find_all(
        'div', {'class':['StoreRow-wrapper_32933b82','StoreRow-complete_f20e8e33']})


    try:
        for i in epic:
            link = i.find(
                'a',{'class':['StoreCard-card_c451165d','StoreCard-tall_78db8e38']})['href']
            # for steam in soup.find_all('a',{'class':'tab_item'}): # return as a list
            print(link)


            session = requests.Session()
            session.headers = {
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
            url = 'https://www.epicgames.com'+link

            content = session.get(url, verify=False).content

            soup = BeautifulSoup(content, "html.parser")

            title = soup.find(
                'h1',{'class':'NavigationVertical-subNavLabel_1428bd43'}).text
            print(title)
            tags = soup.find(
                'div',{'class':['GameMeta-data_190d6d22','GameMeta-listData_76d672d8']})
            print(tags)
            price=soup.find('span',{'class':''})
            print(price)
            gametags = []
            for u in tags:
                gametags.append(u)
                print(gametags)



    except:
        pass

gog()

"""



def steam(request):

        pages = [2,3,4,5,6]
        
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
                    price = soup.find('div',{'class':'game_purchase_price'}).text
                    newprice = price.strip()
                    
                    if newprice == 'Free to Play':
                        finalprice = 00.00

                    else:
                        finalprice = (Decimal(newprice.strip('RM')))

                    print(finalprice)
                    tags = soup.find_all('a',{'class':'app_tag'})
                    arraytags=[]
                    for i in tags:
                        arraytags.append(i.string.strip())
                    print(arraytags)

                    
                    image = soup.find('img', {'class': 'game_header_image_full'})['src']       
                    media_root = '/FYP/django/rise/media'
                    if not image.startswith(("data:image", "javascript")):
                        #local_filename = image.split('/')[-1].split("?")[0]
                        local_filename = title+'.jpg'
                        r = session.get(image, stream=True, verify=False)
                        with open(local_filename, 'wb') as f:
                            for chunk in r.iter_content(chunk_size=1024):
                                f.write(chunk)

                        current_image_absolute_path = os.path.abspath(local_filename)
                        shutil.move(current_image_absolute_path, media_root)

                    print(local_filename)




                    
                except:
                    pass

                for row in Steam.objects.all():
                    if  Steam.objects.filter(gametitle=row.gametitle).count() > 1:
                        row.delete()

                new_steam = Steam()
                new_steam.gametitle=title
                new_steam.price=finalprice
                new_steam.url=link
                new_steam.rating=metascore  
                new_steam.image=local_filename
                new_steam.tag=arraytags
                new_steam.save()

        context = {
            'steams': Steam.objects.all()
        }

        return render(request, 'steam/gamescrape.html', context)



"""

        topseller = soup.find('div', {'id': 'tab_content_ConcurrentUsers'})
        steam = topseller.find_all('a', {'class': 'tab_item'})

        for i in steam:

            # for steam in soup.find_all('a',{'class':'tab_item'}): # return as a list

            title = i.find('div', {'class': 'tab_item_name'}).text
            print(title)
        
        price = i.find('div', {'class': 'discount_final_price'}).text
        if price == 'Free to Play':
            newprice = 00.00
        else:
            newprice = (Decimal(price.strip('RM')))
            # print(newprice)
            image = i.find('img', {'class': 'tab_item_cap_img'})['src']
            tags = i.find_all('span', {'class': 'top_tag'})

            gametags = []
            for u in tags:
                gametags.append(u.string.replace(",", " "))

            # print(gametags)

            media_root = '/FYP/django/rise/media'
            if not image.startswith(("data:image", "javascript")):
            # local_filename = image.split('/')[-1].split("?")[0]
                local_filename = title+'.jpg'
            r = session.get(image, stream=True, verify=False)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)

            current_image_absolute_path = os.path.abspath(local_filename)
            shutil.move(current_image_absolute_path, media_root)

        link = i['href']

        session = requests.Session()
        session.headers = {
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
        url = link

        content = session.get(url, verify=False).content

        soup = BeautifulSoup(content, "html.parser")

        metascore = soup.find('meta', {'itemprop': 'ratingValue'})[
            'content']

        new_steam = Steam()
        new_steam.gametitle = title
        new_steam.tag = gametags
        new_steam.price = newprice
        new_steam.image = local_filename
        new_steam.url = link
        new_steam.rating = metascore
        new_steam.save()

    context = {
        'steams': Steam.objects.all()
    }

    return render(request, 'steam/gamescrape.html', context)




def gog():

    session = HTMLSession()
    #session = requests.Session()
    r = session.get('https://www.humblebundle.com/store/search?sort=bestselling&genre=Action')
    
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://www.gog.com/games?sort=popularity&page=1&category=action'

    content = session.get(url, verify=False).content
     
    soup = BeautifulSoup(content, "html.parser")
    
    topseller = soup.find_all('div', {'class': 'product-tile'})
    for i in topseller:
        title = i.find('a', {'class': ['product-tile__content','js-content']})['ng-href']
        print(title)
    
    r.html.render()
    gog = r.html.find('.base-main-wrapper')
    print(gog)

gog()
"""

def Gamelist(request):

    context = {
        'steams': Steam.objects.all()
    }

    return render(request, 'steam/gamelist.html', context)
"""
def rotten():

            session = requests.Session()
            session.headers = {
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
            url = 'https://www.rottentomatoes.com/top/bestofrt/'

            content = session.get(url, verify=False).content
            soup = BeautifulSoup(content, "html.parser")

            body = soup.find('table',{'class':'table'})
            rotten = body.find_all('tr')
            for i in rotten:
                text = i.find('a',{'class':'articleLink'})
                soup3 = BeautifulSoup(str(text), 'lxml')
                print(soup3.text.strip())



rotten()
"""
