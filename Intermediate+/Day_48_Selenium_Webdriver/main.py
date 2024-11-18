from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dotenv import load_dotenv
import os
import time

def wait_for_page_to_load(timeout=30):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

load_dotenv(".env")

options = Options()
options.binary_location = os.getenv("FIREFOX_EXEC_PATH")

gecko_path = os.getenv("GECKO_PATH")
service = Service(executable_path= gecko_path)

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.wuxiaworld.site")

wait = WebDriverWait(driver, 15)

sign_in = driver.find_element(By.CSS_SELECTOR, ".c-sub-nav_wrap > div:nth-child(2) > a:nth-child(1)").click()

user_details = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#loginform input")))
user_details[0].send_keys("psuswin00@gmail.com")
user_details[1].send_keys("Su$i0410")

submit = driver.find_element(By.CLASS_NAME, "submit").click()

time.sleep(10)

sidebar = driver.find_element(By.CLASS_NAME, "sidebar-col")

popular_today = sidebar.find_element(By.CLASS_NAME, "widget-content")

novel_list = popular_today.find_elements(By.CLASS_NAME, "popular-item-wrap")

print(len(novel_list))

main_tab_hande = driver.current_window_handle

for novel in novel_list[:8]:
    a_tag = novel.find_element(By.TAG_NAME, "a")
    link = a_tag.get_attribute("href")
    title = a_tag.text
    driver.execute_script(f"window.open('{link}', '_blank');")
    driver.switch_to.window(driver.window_handles[1])
    wait_for_page_to_load()
    
    try:
        comments = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/span")))
        count = int(comments.text.split(" ")[0])
        if count < 100:
            driver.close()
        else:
            print(f"{comments.text} found in this tab.")
            bookmark = driver.find_element(By.CSS_SELECTOR, ".wp-manga-action-button").click()
    except NoSuchElementException:
        print("Element not found")
        driver.close()
    except TimeoutException:
        print(f"Element not found within timeout for {title}")
        driver.close()     

    driver.switch_to.window(main_tab_hande)

    time.sleep(1)
    
    print(f"Switched back to main tab after processing link")


# Scrape data from python.org:

# driver.get('https://www.python.org/')

# events = driver.find_element(By.CLASS_NAME, 'event-widget')
# list_elements = events.find_elements(By.TAG_NAME, 'li')

# event_dict = {}
# i = 0

# for event in list_elements:
#     date = event.find_element(By.TAG_NAME, 'time').text
#     name = event.find_element(By.TAG_NAME, 'a').text
#     temp_dict = {
#         'time': date,
#         'name': name,
#     }
#     event_dict[i] = temp_dict
#     i += 1

# print(event_dict)


# driver.quit()

