import shutil
import ntpath
import os.path
import os
from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
requests.packages.urllib3.disable_warnings()

from .models import Steam


def steam(request):

    session = requests.Session()
    session.headers = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://store.steampowered.com/tags/en/Massively%20Multiplayer/#p=0&tab=TopSellers'

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html.parser")

    topseller = soup.find('div', {'id': 'tab_content_TopSellers'})
    steam = topseller.find_all('a', {'class': 'tab_item'})

    for i in steam:
        
            # for steam in soup.find_all('a',{'class':'tab_item'}): # return as a list

            title = i.find('div', {'class': 'tab_item_name'}).text
            price = i.find('div', {'class': 'discount_final_price'}).text
            image = i.find('img', {'class': 'tab_item_cap_img'})['src']
            """
            tags = i.find_all('span', {'class': 'top_tag'})

            for u in tags:
                gametag=u.string
                new_steam = Steam()
                new_steam.tag=tags

            """
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
   
    
            new_steam = Steam()
            new_steam.gametitle= title
            #new_steam.url= url
            new_steam.price= price
            new_steam.image= local_filename
            new_steam.save()
    
        
    return render(request, 'steam/news.html')
# Create your views here.
#steam()