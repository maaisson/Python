from bs4 import BeautifulSoup 
import requests
import pandas as pd
import sqlite3

url = "https://lista.mercadolivre.com.br/lava-lou%C3%A7as-electrolux-14-servi%C3%A7os-220v#D[A:lava%20lou%C3%A7as%20electrolux%2014%20servi%C3%A7os%20220v]"
items = 50
response = requests.get(url).text

parsed = BeautifulSoup(response, 'html.parser')

products = parsed.find_all('li', class_='ui-search-layout__item shops__layout-item')

for product in products:
    name = product.find('h3', class_='poly-component__title-wrapper').text
    price = product.find('span', class_='andes-money-amount andes-money-amount--cents-superscript').text
    print(name, '|', price)

