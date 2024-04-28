import time
from selenium import webdriver

browser = webdriver.Chrome()

# get()
browser.get('https://google.com')

# maximize_window()
browser.maximize_window()

time.sleep(3)

# refresh() (F5)
browser.refresh()

time.sleep(3)

browser.get('https://youtube.com')

time.sleep(2)

# back() (retornar a pagina)
browser.back()

time.sleep(2)

# forward() (vai para a pagina que tinha acessado)
browser.forward()

time.sleep(3)

# close() fecha a aba que esta sendo utilizado
browser.switch_to.new_window("tab") # ->  criando uma nova aba
time.sleep(2)

browser.close()
time.sleep(2)

# quit() (mata todo processo muito utilizado)
browser.quit()
