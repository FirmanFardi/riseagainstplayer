from .models import Steam
from genre.models import Genre
from developer.models import Developer
from tag.models import Tag
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


def steam(request):



    Steam.objects.all().delete()
    Developer.objects.all().delete()
    Tag.objects.all().delete()
    Genre.objects.all().delete()


    pages = [2,3]
    
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

            tags_list = list()        

            
            try:
                metascore = soup.find('meta', {'itemprop': 'ratingValue'})['content']
                print(metascore)
                title = soup.find('div',{'class':'apphub_AppName'}).text
                print(title)
                genre = soup.find('div',{'class':'details_block'}).a.text
                print(genre)
                developer = soup.find('div',{'class':'dev_row'}).a.text
                print(developer)
                price = soup.find('div',{'class':'game_purchase_price'}).text
                newprice = price.strip()
                
                if newprice == 'Free to Play':
                    finalprice = 00.00

                else:
                    finalprice = (Decimal(newprice.strip('RM')))

                print(finalprice)

                image = soup.find('img', {'class': 'game_header_image_full'})['src']       
                media_root = '/home/django/rise/media'
                if not image.startswith(("data:image", "javascript")):
                    #local_filename = image.split('/')[-1].split("?")[0]
                    local_filename = title+'.jpg'
                    r = session.get(image, stream=True, verify=False)
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            f.write(chunk)

                    current_image_absolute_path = os.path.abspath(local_filename)
                    shutil.move(current_image_absolute_path, media_root)

                tags = soup.find_all('a',{'class':'app_tag'})
                
                for i in tags[0:5]:
                    tag=i.string.strip()
                    print(tag)

                    new_tag=Tag()
                    new_tag.name = tag
                    #new_tag.save()
                    


                    if  Tag.objects.filter(name=tag).count() < 1:
                        new_tag.save()
                                                                                                                    
                    new_tag = Tag.objects.get(name=tag)

                    tags_list.append(new_tag)


                print(local_filename)






                new_genre = Genre()
                new_genre.name = genre
                #new_genre.save()

                if  Genre.objects.filter(name=genre).count() < 1:
                    new_genre.save()
                                                                                                                    
                new_genre = Genre.objects.get(name=genre)
                                                         
                
                new_developer = Developer()
                new_developer.name = developer
                #new_developer.save()

                if  Developer.objects.filter(name=developer).count() < 1:
                    new_developer.save()
                                                                                                                    
                new_developer = Developer.objects.get(name=developer)


            
                new_steam = Steam()
                new_steam.gametitle=title
                new_steam.genre=new_genre
                new_steam.developer=new_developer
                new_steam.price=finalprice
                new_steam.url=link
                new_steam.rating=metascore  
                new_steam.image=local_filename
                new_steam.save() 

                for tag in tags_list:
                    new_steam.tags.add(tag)



                for row in Steam.objects.all():
                    if  Steam.objects.filter(gametitle=row.gametitle).count() > 1:
                        row.delete()

            
            except:
                pass






    context = {
        'steams': Steam.objects.all()
        }

    return render(request, 'steam/gamescrape.html', context)


    """
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

        for row in Steam.objects.all():
            if  Steam.objects.filter(gametitle=row.gametitle).count() > 1:
                row.delete()

        new_steam = Steam()
        new_steam.gametitle=newtitle
        new_steam.price=finalprice
        new_steam.url=link 
        new_steam.image=local_filename
        new_steam.tag=newtag
        new_steam.save()
    """


"""
def uplay(request):

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
    link = game.find_elements_by_xpath("//div[@class='product-tile card    full-tile-link']/a[@href]")

    for post in link:
        print ( post.get_attribute("href"))


        



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

"""

def Gamelist(request):

    context = {
        'steams': Steam.objects.all()
    }

    return render(request, 'steam/gamelist.html', context)






