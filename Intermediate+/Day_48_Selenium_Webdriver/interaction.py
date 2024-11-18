from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv(".env")

option = Options()
option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

gecko_path = os.getenv("GECKO_PATH")
service = Service(executable_path=gecko_path)

browser = webdriver.Firefox(options=option, service=service)

browser.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)

cookies = browser.find_element(By.CSS_SELECTOR, ".cc_btn")
cookies.click()
# print(cookies)

time.sleep(2)

lang = browser.find_element(By.ID, "langSelect-EN")
lang.click()

time.sleep(2)

cookie_button = browser.find_element(By.ID, "bigCookie")

timeout = time.time() + 60*5

while True:
    cookie_button.click()

    score_text = browser.find_element(By.ID, "cookies").text.split(" ")
    score = int(score_text[0])
    speed = float(score_text[-1])

    if time.time() > timeout:
        print(speed)
        break

    upgrades = browser.find_element(By.CSS_SELECTOR, "#products")
    products = upgrades.find_elements(By.CLASS_NAME, "enabled")

    values = []
    cost = []
    for product in products:
        value = product.text.split('\n')[-1]
        key = product.get_attribute('id')
        values.append((key, value))
        cost.append(value)

    if cost:
        min_cost = min(cost)
    
    for item in values:
        if item[1] == min_cost:
            p_id = item[0]
            selected = browser.find_element(By.ID, f"{p_id}")
            selected.click()

browser.quit()