from django.test import TestCase

import requests
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='4bc9bcf900c046e1949c3d31f71313ec')

def news():

    url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        '4bc9bcf900c046e1949c3d31f71313ec')
    response = requests.get(url)
    print (response.json())


news()

