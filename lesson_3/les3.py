import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        'user-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0'
    }

    req = requests.get(url, headers)
    with open('index.html', 'w') as file:
        file.write(req.text)

get_data('http://www.edutainme.ru/edindex/')