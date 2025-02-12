from bs4 import BeautifulSoup
import requests
import csv

csvfilne = ".\\04\\products.csv"

with open(csvfilne, "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nome", "Preço"])

url = "https://lista.mercadolivre.com.br/lava-lou%C3%A7as-electrolux-14-servi%C3%A7os-220v#D[A:lava%20lou%C3%A7as%20electrolux%2014%20servi%C3%A7os%20220v]"

response = requests.get(url).text

parsed = BeautifulSoup(response, "html.parser")

while next_page := parsed.find("a", class_="andes-pagination__link", title="Seguinte"):

    products = parsed.find_all("li", class_="ui-search-layout__item shops__layout-item")
    
    with open(csvfilne, "a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        
        for product in products:
            name = product.find("h3", class_="poly-component__title-wrapper").text
            price = product.find("span", class_="andes-money-amount andes-money-amount--cents-superscript").text
            writer.writerow([name, price])
        
    next_page = parsed.find("a", class_="andes-pagination__link", title="Seguinte")
    print(next_page)
    if parsed.find("span", class_='andes-pagination__arrow-title'):
        url = next_page["href"]        
        print(next_page)   
        response = requests.get(url).text
        parsed = BeautifulSoup(response, "html.parser")
    else:
        print("Fim da execução")
        print(next_page)
        break

print("Fim da execução")
        
