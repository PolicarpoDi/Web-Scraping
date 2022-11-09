from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(r'.\chromedriver.exe')

browser.get("https://www.linkedin.com/login")

# Busca o elemendo ID username
input_email = browser.find_element(By.ID, "username")
# Insere o valor da variavel
input_email.send_keys(login)

# Busca o elemendo ID password
input_password = browser.find_element(By.ID, "password")
# Insere o valor da variavel
input_password.send_keys(senha)

# Busca no DOM pelo metodo XPATH o elemento button, do tipo submit
b_login = browser.find_element(By.XPATH, "//button[@type='submit']")
b_login.click()

# Busca no DOM pelo metodo XPATH o elemento input, do placeholder Pesquisar
busca = browser.find_element(By.XPATH, "//input[@placeholder='Pesquisar']")
busca.send_keys('Python')
busca.send_keys(Keys.RETURN)

time.sleep(5)

# Busca no DOM pelo metodo XPATH o elemento button, aria-pressed = vagas
b_vagas = browser.find_element(By.XPATH, "//button[@aria-pressed='false']")
b_vagas.send_keys(Keys.RETURN)

input('')