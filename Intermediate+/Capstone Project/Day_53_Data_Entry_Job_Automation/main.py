from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os
from bs4 import BeautifulSoup
import requests

load_dotenv("../../.env")

url = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
}

response = requests.get(url=url, headers=header)

contents = response.text
soup = BeautifulSoup(contents, "html.parser")
all_property = soup.find(class_ = "List-c11n-8-84-3-photo-cards")
property_list = all_property.find_all(class_ = "ListItem-c11n-8-84-3-StyledListCardWrapper")

property_links = []
prices = []
addresses = []

for prop in property_list:
    a_link = prop.find("a")
    ref_link = a_link.get('href')
    price = prop.find(name = "span", class_ = "PropertyCardWrapper__StyledPriceLine").text.split('+')[0].split('/')[0]
    address = prop.find("address").text.strip()
    property_links.append(ref_link)
    prices.append(price)
    addresses.append(address)


option = Options()
option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

services = Service(executable_path=os.getenv("GECKO_PATH"))

driver = webdriver.Firefox(options=option, service=services)

for i in range(0, len(prices)):

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScW4qfJgfaIk27kmOY0Lf7Lm9QUx8gSfYz3n0J3qirB5-V6VA/viewform?usp=sf_link")
    # driver.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-130.81589735937501%2C%22east%22%3A-114.050760640625%2C%22south%22%3A35.43853743862058%2C%22north%22%3A40.04045948650285%7D%2C%22mapZoom%22%3A6%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22usersSearchTerm%22%3A%22%22%7D")

    main_tab_handle = driver.current_window_handle
    print(main_tab_handle)

    wait = WebDriverWait(driver, 15)

    inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".whsOnd")))
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(property_links[i])

    submit = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]')
    submit.click()

    time.sleep(3)