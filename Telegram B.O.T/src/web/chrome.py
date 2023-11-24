import getpass
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.controller.bet import Bet


class Chrome:

    def Driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("user-data-dir=C:\\Users\\" + getpass.getuser(
        ) + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1024, 650)
        return driver

    def Watch(driver):
        previous_child_count = len(driver.find_elements(
            By.XPATH, "//div[@class='message-date-group']/*"))
        while True:
            current_child_count = len(driver.find_elements(
                By.XPATH, "//div[@class='message-date-group']/*"))
            if current_child_count > previous_child_count:
                Bet.TrateMessage(driver.find_elements(By.XPATH, "//div[@class='message-date-group']/*"))
                previous_child_count = current_child_count
            time.sleep(1)
