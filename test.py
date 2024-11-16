from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def startChrome():
    options = webdriver.ChromeOptions() 
    options.add_argument("/Users/benjammunoz/Library/Application Support/Google/Chrome/Person 1")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    return driver

driver = startChrome()
url = 'https://sodimac.falabella.com/sodimac-cl'
driver.get(url)

