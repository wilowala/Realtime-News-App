import json
import requests
from app.models import Source, News

api_key  = '6f7d710849704d7e900ffe692bd89900'
base_url ='https://newsapi.org/v2/top-headlines?q=news&apiKey={}'
sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
local_url = 'https://newsapi.org/v2/everything?q=kenya&apiKey={}'

def configure_request(app):
    global api_key,base_url, sources_url, local_url, africa_url

def get_news():
    """NEWS API Call"""
    url = base_url.format(api_key)
    response = requests.get(url).json()
    return response['articles']

def get_sources():
    """SOURCES API Call"""
    url = sources_url.format(api_key)
    response = requests.get(url).json()
    return response['sources']

def get_local_news():
    """SOURCES API Call"""
    url = local_url.format(api_key)
    response = requests.get(url).json()
    return response['articles']