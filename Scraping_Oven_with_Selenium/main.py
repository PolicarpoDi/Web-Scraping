from bs4 import BeautifulSoup
from selenium import webdriver

import time

from termcolor import colored as cores

driver = webdriver.Firefox()

url = 'https://www.americanas.com.br/produto/129019474?pfm_index=NaN&pfm_page=category&pfm_pos=grid&pfm_type=category_page&cor=Preto&voltagem=220V&condition=NEW'

driver.get(url)

time.sleep(5)

div_mae = driver.find_element('css selector', "main[class='src__Container-sc-m79eh9-0 bcPhXp Product']")

html_content = div_mae.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')

lista_preco = soup.find.all('div', class_="styles__PriceText-sc-x06r9i-0 dUTOlD priceSales")

lista_descricao = soup.find.all('h1', class_="product-title__Title-sc-1hlrxcw-0 jyetLr")

print(f'Descrição: {lista_descricao}, Preço: {lista_preco}')