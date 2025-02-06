import requests
from bs4 import BeautifulSoup

link = "https://www.olx.kz/elektronika/igry-i-igrovye-pristavki/pristavki/karaganda/?search%5Bfilter_enum_console_manufacturers%5D%5B0%5D=2272"

response = requests.get(link).text
soup = BeautifulSoup(response, 'lxml')

items = soup.find('div', class_='css-j0t2x2')
title = items.find_all('h4', class_='css-1sq4ur2')
price = items.find_all('p', class_='css-6j1qjp')

for i in range(len(title)):
    with open('consoles.txt', 'a', encoding='utf-8') as file:
        file.write(f'{title[i].text} - {price[i].text}\n')
