import re

from bs4 import BeautifulSoup

with open('blank/index2.html') as file:
    src = file.read()  # сохранение содержимого в src

soup = BeautifulSoup(src, 'lxml')  # lxml название парсера

# title = soup.title  # получения <title>
# print(title.text)  # (title.string) получение содержимого <title>
# .find() - ищет первое совпадение
# find_all() - ищет все совпадения
# page_h1 = soup.find('h1')
# print(page_h1)
#
# page_all_h1 = soup.find_all('h1')
# print(page_all_h1)
# for item in page_all_h1:
#     print(item.text)  # получение содержимого тега


# user_name = soup.find('div', class_='user__name')  #поиск class_='user__name'в <di> /html/body/div/div[2 ибп]/div[2]/div[2 ибп]/span
# print(user_name.text.strip())

# user_name = soup.find('div', class_='user__name').find('span').text
# print(user_name)

# user_name = soup.find('div', {'class': 'user__name'}).find('span').text  # поиск при помощи словаря
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_= 'user__info').find_all('span') #поиск всех 'span'
# print(find_all_spans_in_user_info)
# for item in find_all_spans_in_user_info:
#     print(item.text) #выводит на печать все span

# ! парсинг соц сетей
# social_links = soup.find(class_='social__networks').find('ul').find_all('a')
# for item in social_links:
#     print(item)
# print(social_links)

# all_a = soup.find_all('a')  # поиск всех тегов 'a'
# for item in all_a:
#     item_url = item.get('href') # цикл для отображения только ссылок!
#     print(item_url)

# all_a = soup.find_all('a')  # поиск всех тегов 'a'
# for item in all_a:
#     item_text = item.text
#     item_url = item.get('href') # цикл для отображения только ссылок!
#     print(f'{item_text}:{item_url}') # добавлние названия соц сети

# .find_parent() .find_parents() поиск родителя элемента (снизу-вверх)
# post_div = soup.find(class_='post__text').find_parent()  # поиск родителя class_='post__text'
# print(post_div)

# post_div = soup.find(class_='post__text').find_parents()  #
# print(post_div)


# ! next_element previous_element  движение по коду
# next_el = soup.find(class_='post__title').next_element.next_element.text  # поиск названия статьи(нужно вызвать повторно!)
# print(next_el)
# next_el = soup.find(class_='post__title').find_next().text  # поиск названия статьи похожий метод
# print(next_el)


# ! find_next_sibling()  find_previous_sibling()  возвращают след и предыдущий элемент внутри искомого тега
# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

# links = soup.find(class_='some__links').find_all('a')
# print(links)
# for link in links:
#     link_href_attr = link.get('href')  # = link['href']
#     link_data_attr = link.get('data-attr')  # = link['data-attr']
#     print(link_href_attr)
#     print(link_data_attr)

# ! поиск текста
# find_text = soup.find('a', text=re.compile('Одежда')) # !re - модуль регулярных выражений
# print(find_text)

find_all = soup.find_all(text=re.compile('([Оо]дежда)'))  # поиск текста везде в 2 регистрах
print(find_all)
