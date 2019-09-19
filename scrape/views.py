from django.shortcuts import render
import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup

import os
import os.path
import ntpath
import shutil
from .models import Scraper

def scrape1(request):


    session = requests.Session()
    session.headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://sea.ign.com/'

    content = session.get(url, verify=False).content
    
    soup = BeautifulSoup(content, "html.parser")

    posts = soup.find_all('article',{'class':'card NEWS p1'}) # return as a list
    
    for i in posts:

        title= i.find_all('h3',{'class':'caption'})[0].text
        image_source = i.find('img',{'class':'thumb'})['src']
        
        media_root = '/FYP/django/rise/media'
        if not image_source.startswith(("data:image", "javascript")):
            local_filename = image_source.split('/')[-1].split("?")[0]
            r = session.get(image_source, stream=True, verify=False)
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            
            current_image_absolute_path = os.path.abspath(local_filename)
            shutil.move(current_image_absolute_path,media_root)
        

        new_scrape = Scraper()
        new_scrape.title1= title
        new_scrape.image1=local_filename
        new_scrape.save()

    return render(request, '/admin')



# Create your views here.
