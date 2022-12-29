from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import requests
from bs4 import BeautifulSoup
import smtplib
from termcolor import colored as cores
import time
from decouple import config


url = 'https://www.mercadolivre.com.br/forno-de-embutir-eletrico-brastemp-boc84-84l-preto-220v/p/MLB9990127?pdp_filters=category:MLB120314#searchVariation=MLB9990127&position=1&search_layout=stack&type=product&tracking_id=9c82cd80-1459-4589-85c9-f674708f14a3'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_ = 'ui-pdp-title').get_text()

price = soup.find_all('span', class_ = 'andes-money-amount__fraction')
price = price[1].get_text().strip()

num_price = price.replace('R$', '')
num_price = num_price.replace('.','')
num_price = float(num_price)


def send_email():
    with open('template.html', 'r') as html:
        template = Template(html.read())
        data = datetime.now().strftime('%d/%m/%Y')
        corpo_msg = template.substitute(nome=config('SeuNome'), data=data, descricao=title, preco=price, link=url) 
    
    msg = MIMEMultipart()
    # Email que vai enviar
    msg['from'] = config('meu_email') 
    # Email que vai receber
    msg['to'] = config('destino_email')    
    # Titulo
    msg['subject'] = f'Monitoramento detectou o produto {title} abaixo do preço procurado.'

    corpo = MIMEText(corpo_msg, 'html')
    # Envia o corpo do email
    msg.attach(corpo) 
    
    smtp = smtplib.SMTP(config('host_smtp'), config('porta'))
    smtp.starttls()
    smtp.login(config('meu_email'), config('minha_senha'))
    smtp.sendmail(config('destino_email'), config('meu_email'), msg.as_string())


with smtplib.SMTP(host=config('host_smtp'), port=config('porta')) as smtp:
    if (num_price < 2800):
        try:
            send_email()
            print(cores(f'Produto encontrado com sucesso!!!!', 'green'))
            print('E-mail sendo encaminhado...')
            time.sleep(5)
            print('E-mail enviado com sucesso!.')
        except Exception as e:    
            print(cores('E-mail não enviado...', 'red'))
            print('Erro: ', e)
