from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv("../.env")

class AutoTinderBot:
    def __init__(self, url):
        self.option = Options()
        self.option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

        self.services = Service(executable_path=os.getenv("GECKO_PATH"))

        self.driver = webdriver.Firefox(options=self.option, service=self.services)

        self.driver.get(url)
        
        main_tab_handle = self.driver.current_window_handle
        print(main_tab_handle)

        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.c1p6lbu0")))
        login.click()

        time.sleep(5)
        more_opt = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.Td\(u\)")))
        if more_opt:
            more_opt.click()

        time.sleep(5)
        ph_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.My\(12px\):nth-child(3) > button")))
        ph_btn.click()

        input("press enter after you lear the captcha...")

        ph_num = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#phone_number")))
        ph_num.send_keys(os.getenv("PHONE_NUMBER"))

        next_btn = self.driver.find_element(By.CSS_SELECTOR, ".W\(70\%\)")
        next_btn.click()

        input("press enter after you lear the captcha...")

        otp_num = input("Enter OTP: ")

        otp_list = [n for n in otp_num]

        for i in range(6):
            num = self.driver.find_element(By.CSS_SELECTOR, f"div.c41febb:nth-child({i+1}) > div:nth-child(3) > input").send_keys(f"{otp_list[i]}")

        proceed = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".W\(70\%\)")))
        proceed.click()

        send_code = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.c1p6lbu0:nth-child(5)")))
        if send_code:
            print("Found")
        else:
            print("not found")

        self.driver.execute_script("arguments[0].click();", send_code)

        input("press enter to proceed...")

        code = input("Enter code: ")

        code_list = [n for n in code]

        final_num = self.driver.find_element(By.CSS_SELECTOR, "div.c41febb:nth-child(6) > div:nth-child(3) > input:nth-child(1)")
        for i in range(6):
            num = self.driver.find_element(By.CSS_SELECTOR, f"div.c41febb:nth-child({i+1}) > div:nth-child(3) > input:nth-child(1)").send_keys(f"{code_list[i]}")

        proceed_2 = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.c1p6lbu0:nth-child(2)")))

        try:
            self.driver.execute_script("arguments[0].click();", proceed_2)
        except ElementClickInterceptedException:
            print("There is an error. Proceeding anyway...")
            pass

    def permissions(self):
        input("press enter after selecting language...")

        allow_location = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.c1p6lbu0:nth-child(1)")))
        self.driver.execute_script("arguments[0].click()", allow_location)

        input("press enter after allowing access...")

        notification = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.c1p6lbu0:nth-child(2)")))
        self.driver.execute_script("arguments[0].click()", notification)

        input("press enter to proceed...")

    def swipe(self):
        try:
            like_btn_div = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.gamepad-button-wrapper:nth-child(4)")))
            like_btn = like_btn_div.find_element(By.TAG_NAME, "button").click()
        except NoSuchElementException:
            time.sleep(2)
            print("exception has occured...")
        

url = "https://tinder.com"

if __name__ == "__main__":
    bot = AutoTinderBot(url)
    bot.login()
    bot.permissions()

    input("press enter to start...")
    time.sleep(10)

    for i in range(100):
        bot.swipe()
        i += 1
        print(f"{i} times completed")
        time.sleep(2)
