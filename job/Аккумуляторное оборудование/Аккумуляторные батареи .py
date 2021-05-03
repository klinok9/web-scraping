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

# #парсинг и сохранение страницы
# url = "https://electro-shop.ru/akkumulyatornoe_oborudovanie/"
# req = requests.get(url, headers=headers)
# src = req.text
# with open('index.html', 'w')as file: # запись страницы в файл
#     file.write(src)
# with open('index.html')as file:  # чтение сохран страницы
#     src = file.read()
#
# dictionary = {}
# # поиск наименования и цены!!!
# soup = BeautifulSoup(src, 'lxml')
# name_of_item = soup.find_all(class_='catalog-section-item')
# for item in name_of_item:
#     name = item.h2.text
#     # name = soup.find('h2')
#     price = item.span.text
#     print(f'{name}: {price}')
#     dictionary[name] = price
#     #запись в csv
#     with open("1.csv", "a", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (
#                 name,
#                 price
#             )
#         )





# парсинг страниц в разделе аккум бат
for i in range(48,49):
    url = f'https://electro-shop.ru/akkumulyatornoe_oborudovanie/?PAGEN_1={i}'
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

    # soup = BeautifulSoup(src, 'lxml')
    # name_of_item = soup.find_all('h2')
    # price = soup.find_all(class_='catalog-price')
    # for item in price:
    #     print(item.text.strip())
    # for item in name_of_item:
    #     print(item.text.strip())
    # print(name_of_item)

# with open('name.json', 'w') as file:
#     json.dump(name_of_item, file , indent=4, ensure_ascii=False)
# with open(f'data/index{i}.html', 'w')as file:  # запись страницы в файл
#     file.write(name_of_item)
    sleep(random.randrange(1, 2))
    # with open('index.html')as file:  # чтение сохран страницы
    #     src = file.read()

