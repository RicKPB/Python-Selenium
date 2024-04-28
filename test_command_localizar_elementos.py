import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()

browser.get('https://www.saucedemo.com/')

# username = browser.find_element(By.ID, 'user-name')
# password = browser.find_element(By.ID, 'password')

# username.send_keys('standard_user')
# password.send_keys('secret_sauce')

auth_fields = browser.find_elements(By.XPATH, '//*[@class="input_error form_input"]')
print(auth_fields)
print(len(auth_fields))

time.sleep(5)
