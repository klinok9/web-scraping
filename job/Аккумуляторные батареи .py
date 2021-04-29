import requests
from bs4 import BeautifulSoup
import json
import random
import csv
from time import sleep

headers = {'Accept':'*/*',
           'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}


# url = "https://electro-shop.ru/akkumulyatornoe_oborudovanie/"
# req = requests.get(url, headers=headers)
# src = req.text
# with open('index.html', 'w')as file: # запись страницы в файл
#     file.write(src)
with open('index.html')as file:  # чтение сохран страницы
    src = file.read()


#поиск наименования
soup = BeautifulSoup(src, 'lxml')
name_of_item = soup.find_all('h2')
for item in name_of_item:
    print(item.text.strip())


#поиск цены
price = soup.find_all(class_='catalog-price')
for item in price:
    print(item.text.strip())
