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

class FlaskAppBot:
    def __init__(self):
        self.option = Options()
        self.option.binary_location = os.getenv("FIREFOX_EXEC_PATH")

        self.services = Service(executable_path=os.getenv("GECKO_PATH"))

        self.driver = webdriver.Firefox(options=self.option, service=self.services)

        self.driver.get("http://127.0.0.1:5000")

        main_tab_handle = self.driver.current_window_handle
        print(main_tab_handle)

        self.wait = WebDriverWait(self.driver, 15)

app = FlaskAppBot()