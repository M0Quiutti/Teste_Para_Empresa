import time 
import requests
import pandar as pd
from bs4 import BeatifulSoup
from selenuium import webdriver
from selenum.webdriver.firefox.options import options
import json

# 1. Pegar conteúdo HTML a partir da URL
url = ""

option = Options()
option.headless = true
driver = webdriver.Firefox(options=option)

driver.get(url)

time.sleep(5)

driver.find_element_by_xpath("//div[@class='instrument-header-details']//div//div[@data-text='ionstrument-price-last']")

element = driver.find_element_by_xpath("//div[@class='intrument-header-details]//div")
html_content = element.get_atribute('outherHTML')

#2. Parsear o conteúdo HTML - BeaultifulSuop
soup = BeatifulSoup(html_content, 'html.parser')
div = soup.find(name='div')


driver.quit()