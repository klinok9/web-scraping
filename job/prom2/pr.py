import requests
from bs4 import BeautifulSoup
import json
import random
import csv
from time import sleep

headers = {'Accept':'*/*',
           'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}  # симуляция браузера
# #

for i in range(1,175):
    url = f'http://www.oaontc.ru/services/registers/lnk/?&page={i}'
    print(url)
    # url = "http://www.oaontc.ru/services/registers/lnk/"
    req = requests.get(url, headers=headers)
    src = req.text
    print(src)
    with open('index.html', 'w')as file: # запись страницы в файл
        file.write(src)

    with open('index.html')as file: # запись страницы в файл
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    all_hrefs = soup.find(class_="textpage docs").find_all('a')
    print(all_hrefs)
    all_dict = {}

    for item in all_hrefs:
        item_text = item.text
        item_href = 'http://www.oaontc.ru' + item.get('href')

        all_dict[item_text] = item_href

    with open('all_dict.json', 'w') as file:
        json.dump(all_dict, file, indent=4,ensure_ascii=False)

    with open('all_dict.json') as file:
        all_categories = json.load(file)
    print(all_categories)
    #
    # count = 0
    for cat_name, cat_href in all_categories.items():
        # if count == 2:
            req = requests.get(url= cat_href, headers=headers)
            src = req.text

            # with open(f'data/{cat_name}.html', 'w') as file:
            #     file.write(src)
            #
            # with open(f'data/{cat_name}.html') as file:
            #     src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            table_head = soup.find(class_="textpage docs").find_all('tr')
            name = table_head[1].text
            phone = table_head[6].text
            email = table_head[8].text
            phone_lab =  table_head[12].text
            phone_email =  table_head[14].text

            print(name, phone, email, phone_lab, phone_email)


            with open(f'data/1.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow((name, phone, email, phone_lab, phone_email))

            sleep(random.randrange(2,4))