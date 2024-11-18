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

load_dotenv("../.env")

class InstagramFollowerBot:
    def __init__(self):
        self.option = Options()
        self.option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

        self.services = Service(executable_path=os.getenv("GECKO_PATH"))

        self.driver = webdriver.Firefox(options=self.option, service=self.services)

        self.driver.get("https://www.instagram.com/")

        main_tab_handle = self.driver.current_window_handle
        print(main_tab_handle)

        self.wait = WebDriverWait(self.driver, 15)

        self.follower_count = 0

    def login(self):
        email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input")))
        email.send_keys(os.getenv("INSTA_MAIL"))

        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input")))
        password.send_keys(os.getenv("PASSWORD"), Keys.ENTER)

        not_now = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Not now')]")))
        not_now.click()

    def search(self):
        search = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x1xgvd2v > div:nth-child(2) > div:nth-child(2) > span:nth-child(1) > div:nth-child(1) > a")))
        search.click()

        search_text = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".x1lugfcp")))
        search_text.send_keys("cute kittens")

        first_account = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.x1q0g3np:nth-child(1)")))
        first_account.click()

    def follow(self):
        followers = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.xl565be:nth-child(2) > div:nth-child(1) > a:nth-child(1) > span:nth-child(1) > span")))
        self.follower_count = int(followers.text)

        followers_list = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "followers")))
        followers_list.click()

        for i in range(self.follower_count):
            try:
                time.sleep(2)

                follow_btn = self.driver.find_element(By.CSS_SELECTOR, f"div.x1dm5mii:nth-child({i+1}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button")
                follow_btn.click()

                if i == 1:
                    print(f"followed {i} follower")
                else:
                    print(f"followed {i} followers")

                time.sleep(2)

            except (NoSuchElementException, TimeoutException, ElementNotInteractableException) as e:
                print(f"Error following user {i + 1}: {e}")
                continue


if __name__ == "__main__":
    bot = InstagramFollowerBot()
    bot.login()
    bot.search()
    bot.follow()
    print(bot.follower_count)





