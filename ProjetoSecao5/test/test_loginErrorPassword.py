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
password.send_keys("MACACO")
buttonLogin.click()
assert driver.find_element(By.XPATH, '//*[@data-test="error"]').is_displayed()
# --------------------------------------------------
