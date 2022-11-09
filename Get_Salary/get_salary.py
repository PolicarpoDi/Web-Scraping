# Web Scraping com Python

# Realiza requisições 
import requests
# Permite que seja manipulado o html dentro do script
from bs4 import BeautifulSoup
import re

url = 'https://www.glassdoor.com.br/Sal%C3%A1rios/cientista-de-dados-sal%C3%A1rio-SRCH_KO0,18.htm'

# Caso precise enviar de um browser de verdade (tem páginas que não dão acesso para robo
# headers = {'user-agent': 'Mozilla/5.0'}

response = requests.get(url)
sopa_bonita = BeautifulSoup(response.text, 'html.parser')

lista_empresas = sopa_bonita.find_all('h3', {'data-test': re.compile('salaries-list-item-.*-employer-name')})

for empresa in lista_empresas:
    nome_empresa = empresa.find('a').text
    
lista_salarios = sopa_bonita.find_all('div', {'data-test': re.compile('salaries-list-item-.*-salary-info')})

for salario in lista_salarios:
    str_salario = str(salario.find('h3').text)
    
for salario, empresa in zip(lista_salarios, lista_empresas):
    str_salario = str(salario.find('h3').text)
    nome_empresa = empresa.find('a').text
    print(f'A empresa {nome_empresa} esta oferecendo salário de {str_salario}.')