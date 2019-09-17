from django.shortcuts import render
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup

def scrape():
    session = requests.Session()
    session.headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    url = 'https://sea.ign.com/'

    content = session.get(url, verify=False).content
    
    soup = BeautifulSoup(content, "html.parser")

    columns = soup.find_all('article',{'class':'article NEWS'}) # return as a list
    print(len(columns))

scrape()
# Create your views here.
