import requests
from bs4 import BeautifulSoup
import json
import random
import csv
from time import sleep
import openpyxl

headers = {'Accept': '*/*',
           'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
           }

# парсинг страниц в разделе аккум бат
for i in range(1,25):
    url = f'https://electro-shop.ru/stroitelnoe-oborudovanie/?PAGEN_1={i}'
    print(url)
    req = requests.get(url, headers=headers)
    src = req.text
    dictionary = {}
    # поиск наименования и цены!!!
    soup = BeautifulSoup(src, 'lxml')
    name_of_item = soup.find_all(class_='catalog-section-item')
    for item in name_of_item:
        name = item.h2.text
        # name = soup.find('h2')
        price = item.span.text
        print(f'{name}: {price}')
        dictionary[name] = price
        # запись в csv
        with open("1.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    name,
                    price
                )
            )
    sleep(random.randrange(1, 2))
    # with open('index.html')as file:  # чтение сохран страницы
    #     src = file.read()

