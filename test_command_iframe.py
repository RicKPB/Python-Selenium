import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()
browser.get("https://chercher.tech/practice/frames-example-selenium-webdriver")

"""
//*[@type='text']
esse seria um xpath para detectar o Topic dentro do site, que ele esta muito ruim para ser detectado
assim vamos usar um xpath mais detalhado aonde vamos fazer
//*[@id='topic']/following-sibling::input

aqui no caso estaos fazendo com que ele considere como o proximo irmao, assim temos um xpath mais confiavel 
"""

iframe1 = browser.find_element(By.ID, 'frame1')
browser.switch_to.frame(iframe1)
browser.find_element(By.XPATH, '//*[@id="topic"]/following-sibling::input').send_keys('Iframe1')

iframe3 = browser.find_element(By.ID, 'frame3')
browser.switch_to.frame(iframe3)
browser.find_element(By.XPATH, '//*[@id="a"]').click()
time.sleep(5)

# Retornando a raiz da pagina
browser.switch_to.default_content()

iframe2 = browser.find_element(By.ID, 'frame2')
browser.switch_to.frame(iframe2)
seletorAnimals = Select(browser.find_element(By.XPATH, '//select[@id="animals"]'))
seletorAnimals.select_by_value("babycat")
time.sleep(3)
