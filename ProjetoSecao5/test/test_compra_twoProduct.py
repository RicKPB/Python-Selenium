# --------- IMPORTS -------------
from selenium import webdriver
from selenium.webdriver.common.by import By
# -----------------------------

# -------- CRIACAO DE BROWSER --------------------
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/inventory-item.html?id=4')
# ------------------------------------------------

# -------- MAPEAMENTO DE ELEMENTOS -----------------
username = driver.find_element(By.XPATH, '//input[@id="user-name"]')
password = driver.find_element(By.XPATH, '//input[@id="password"]')
buttonLogin = driver.find_element(By.XPATH, '//input[@id="login-button"]')
# --------------------------------------------------

# -------- REALIZACAO DE LOGIN ---------------------
username.send_keys("standard_user")
password.send_keys("secret_sauce")
buttonLogin.click()
# --------------------------------------------------

# -------- ADICIONAR PRODUTO AO CARRINHO 1/CONFERIR SE ADD AO CART ----------------------
item1 = driver.find_element(By.XPATH, '//*[@class="inventory_item_name " and text()="Sauce Labs Backpack"]')
item1.click()
buttonAddCar = driver.find_element(By.XPATH, '//*[text()="Add to cart"]')
buttonAddCar.click()
cart = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
cart.click()
assert driver.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Backpack"]').is_displayed()
# ---------------------------------------------------------------------------------------

# -------- RETORNAR AO SHOPPING --------------------------
continueShopping = driver.find_element(By.XPATH, '//*[@id="continue-shopping"]')
continueShopping.click()
# --------------------------------------------------------

# -------- ADICIONAR PRODUTO AO CARRINHO 2/CONFERIR SE ADD AO CART ----------------------
item2 = driver.find_element(By.XPATH, '//*[@class="inventory_item_name " and text()="Sauce Labs Bike Light"]')
item2.click()
buttonAddCar = driver.find_element(By.XPATH, '//*[text()="Add to cart"]')
buttonAddCar.click()
cart = driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]')
cart.click()
assert driver.find_element(By.XPATH, '//*[@class="inventory_item_name" and text()="Sauce Labs Bike Light"]').is_displayed()
# ---------------------------------------------------------------------------------------

# ------- REALIZACAO DE COMPRA/CONFERENCIA DE COMPRA ------------------------------------
buttonCheckout = driver.find_element(By.XPATH, "//*[@id='checkout']")
buttonCheckout.click()
firstName = driver.find_element(By.XPATH, "//*[@id='first-name']")
firstName.send_keys('Henrique') 
lastName = driver.find_element(By.XPATH, "//*[@id='last-name']")
lastName.send_keys('Bernardo')
codePostal = driver.find_element(By.XPATH, "//*[@id='postal-code']")
codePostal.send_keys('00000-000')
buttonContinue = driver.find_element(By.XPATH, "//*[@id='continue']")
buttonContinue.click()
buttonFinish = driver.find_element(By.XPATH, "//*[@id='finish']")
buttonFinish.click()
assert driver.find_element(By.XPATH, "//*[@class='title' and text()='Checkout: Complete!']")
# ---------------------------------------------------------------------------------------
