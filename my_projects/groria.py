import requests
from bs4 import BeautifulSoup
import json
import random
import csv
from time import sleep

headers = {'Accept':'*/*',
           'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}


# url = "https://www.gloria-jeans.ru/c/boys"
# req = requests.get(url, headers=headers)
# src = req.text
# with open('index.html', 'w')as file: # запись страницы в файл
#     file.write(src)
with open('index.html')as file:  # чтение сохран страницы
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
name_product = soup.find_all('p',class_='list-card__description js-name-product')
for item in name_product:
    print(item.text.strip())
# price = soup.find_all(class_='listing-card__price', attrs='span')
# for item in price:
#     print(item.text.strip())

price_1 = soup.find_all('span',class_='listing-card__price')
for item in price_1:
    print(item.text.strip())
# p = soup.find_all('span',class_='listing-card__price')
# for span in price.span.find_all('span',recursive=False):
#     print(span.text)
# print(name_product)