from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv(".env")

option = Options()
option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

service = Service(executable_path=os.getenv("GECKO_PATH"))

driver = webdriver.Firefox(options=option, service=service)

driver.get("https://www.linkedin.com/login")

main_tab_hande = driver.current_window_handle

time.sleep(5)
email = driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udemy3296@gmail.com")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Su$i0410")

time.sleep(2)
sign_in_button = driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()

input("press enter after captcha!")

time.sleep(5)
jobs = driver.find_element(By.CSS_SELECTOR, "li.global-nav__primary-item:nth-child(3) > a:nth-child(1)").click()

time.sleep(5)
all_search = driver.find_element(By.ID, "global-nav-search")
search_job = all_search.find_element(By.CLASS_NAME, "jobs-search-box__keyboard-text-input").send_keys("Web Developer Intern")
job_location = all_search.find_element(By.CLASS_NAME, "jobs-search-box__text-input--with-clear").send_keys("Chennai, Tamil Nadu, India", Keys.ENTER)

time.sleep(5)
jobs_list = driver.find_element(By.CLASS_NAME, "scaffold-layout__list-container")
all_jobs = jobs_list.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

time.sleep(2)
for job in all_jobs:
    clicker = job.click()

    try:
        time.sleep(5)
        easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button").click()

        time.sleep(5)
        ph_num = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
        if ph_num.text == "":
            ph_num.send_keys("1234567890")
        btn_section = driver.find_element(By.CSS_SELECTOR, "div.justify-flex-end:nth-child(2)")
        next_btn = btn_section.find_element(By.CLASS_NAME, "artdeco-button").click()

        time.sleep(5)
        section_2 = driver.find_element(By.CLASS_NAME, "justify-flex-end")
        next_btn_2 = section_2.find_element(By.CLASS_NAME, "artdeco-button--primary").click()

        time.sleep(5)
        experience = driver.find_elements(By.CSS_SELECTOR, ".artdeco-text-input--input")
        if experience:
            for exp in experience:
                exp.send_keys("1")

        # time.sleep(2)
        # next_btn_3 = driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click()

        # time.sleep(5)
        # radio_div = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/form/div/div")
        # work_opt = radio_div.find_elements(By.TAG_NAME, "label")
        # work_opt[0].click()

            time.sleep(2)
            review = driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click()

            time.sleep(5)
            submit = driver.find_element(By.CLASS_NAME, "artdeco-button--primary").click()
        else:
            close_btn = driver.find_element(By.CSS_SELECTOR, "#ember703")

        time.sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    
    except NoSuchElementException as e:
        print(f"Error applying for job: {e}")
        # driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"Error applying for job: {e}")
        close_btn = driver.find_element(By.CSS_SELECTOR, "#ember703")



