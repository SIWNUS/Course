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

Up_speed_5g = 5.88
Down_dpeed_5g = 4.52

class InternetSpeedTwitterBot:
    def __init__(self):
        self.option = Options()
        self.option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

        self.services = Service(executable_path=os.getenv("GECKO_PATH"))

        self.driver = webdriver.Firefox(options=self.option, service=self.services)

        self.up = 0
        self.down = 0

    def get_internet_speed(self):

        url = "https://www.speedtest.net"
        self.driver.get(url)
        
        main_tab_handle = self.driver.current_window_handle
        print(main_tab_handle)

        self.wait = WebDriverWait(self.driver, 15)

        cont = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#onetrust-accept-btn-handler")))
        cont.click()

        time.sleep(10)
        go_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.js-start-test')))
        go_btn.click()

        input("press enter after allowing location access...")
        time.sleep(60)

        dl_speed = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".download-speed")))
        self.down = dl_speed.text

        ul_speed = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".upload-speed")))
        self.up = ul_speed.text

    def tweet_at_provider(self):
        
        url = "https://x.com/login"
        self.driver.get(url)

        main_tab_handle = self.driver.current_window_handle
        print(main_tab_handle)

        self.wait = WebDriverWait(self.driver, 15)

        time.sleep(10)

        self.login()

        try:
            close_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.r-s8bhmr:nth-child(1) > button")))
            close_btn.click()
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

        post_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-1fkl15p")))
        post_btn.click()

        tweet_area = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='tweetTextarea_0']")))
        tweet_area.send_keys(self.tweet_msg())
        tweet_area.send_keys([Keys.CONTROL, Keys.ENTER])        

    def login(self):
        email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe")))
        email.send_keys(os.getenv("TWITTER_MAIL"), Keys.ENTER)

        username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-30o5oe")))
        username.send_keys(os.getenv("TWITTER_USERNAME"), Keys.ENTER)

        password_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

        while True:
            try:
                password_field.send_keys(os.getenv("PASSWORD"))
                break
            except ElementNotInteractableException:
                print("Password field not interactable. Retrying...")
                time.sleep(5)
                password_field = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))

        login_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-19yznuf")))
        login_btn.click()

    def tweet_msg(self):
        global Up_speed_5g, Down_dpeed_5g
        msg = f"""My 4G internet speed is, Download: {self.down}Mbps and Upload: {self.up}Mbps. My 5G internet speed is, Download: {Down_dpeed_5g}Mbps and Upload: {Up_speed_5g}Mbps. This makes no sense. What is happening, Reliance Jio?"""
        return msg


if __name__ == "__main__":
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    print(f"download speed: {bot.down}\nupload speed: {bot.up}")
    bot.tweet_at_provider()