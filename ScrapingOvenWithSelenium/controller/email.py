from string import Template
from datetime import datetime
from ScrapingOvenWithSelenium.controller.dados_email import *
from main import descricao, preco

#Padrão para enviar email (assunto, to, from)
from email.mime.multipart import MIMEMultipart 
#Corpo do email (texto)
from email.mime.text import MIMEText
#Recebe uma imagem para anexar no email
from email.mime.image import MIMEImage 
import smtplib


def envia_email(corpo_msg):
    with open('template.html', 'r') as html:
        template = Template(html.read())
        data = datetime.now().strftime('%d/%m/%Y')
        corpo_msg = template.substitute(nome=SeuNome, data=data, nome_produto=descricao, preco=preco) # Safe_substitute é usado para não apresentar o erro, mas vai mostrar a variavel
        
        
    msg = MIMEMultipart()
    # Email que vai enviar
    msg['from'] = meu_email 
    # Email que vai receber
    msg['to'] = destino_email    
    # Titulo
    msg['subject'] = 'Monitoramento de preços do forno de embutir 220w' 

    corpo = MIMEText(corpo_msg, 'html')
    # Envia o corpo do email
    msg.attach(corpo) 

    with open('guerra.jpg', 'rb') as img:   # rb = modo de leitura de bytes
        img =  MIMEImage(img.read())
        # Envia a imagem
        msg.attach(img) 


    with smtplib.SMTP(host=host_smtp, port=porta) as smtp:  # Configure o smtp de acordo com o seu servidor de email
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(user=meu_email, password=minha_senha)
            smtp.send_message(msg)
            print('E-mail enviado com sucesso')
        except Exception as e:    
            print('E-mail não enviado...')
            print('Erro: ', e)