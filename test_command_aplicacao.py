import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.saucedemo.com/')

print(f'Titulo: {browser.title}')

print(f'Url: {browser.current_url}')

print(f'Codigo-Fonte: {browser.page_source}')
