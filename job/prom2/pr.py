import requests
from bs4 import BeautifulSoup


person_url_list = []
for i in range(3):
    url= f'http://www.oaontc.ru/services/registers/lnk/?&page={i}'

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find(class_="textpage docs").find_all('a')

    for person in persons:
        person_url = person.get('href')
        print(person_url)
        # person_url_list.append(person_url_list)