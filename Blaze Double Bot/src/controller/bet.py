import json
from selenium.webdriver.common.by import By


class Bet:

    def JsonRead(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    def SetValue(driver):
        # Pode ser que tenha que ser alterado, ele esta achando somente 1 input
        # este loop é errado
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for element in inputs:
            element.send_keys("2.00")

    def ClickColor(driver):
        bets = Bet.JsonRead("../Telegram B.O.T/log/bets.json")
        if bets['color'] == "\u26ab\ufe0f":
            element = driver.find_elements(By.CSS_SELECTOR, "div.black")
            for element2 in element:
                colorclick = element2
        else:
            element = driver.find_elements(By.CSS_SELECTOR, "div.red")
            for element2 in element:
                colorclick = element2
        driver.execute_script("arguments[0].click();", colorclick)

    def Handler(driver):
      elements = driver.find_elements(By.CSS_SELECTOR, "div.place-bet")
      for element in elements:
        button = element.find_element(By.CSS_SELECTOR, "button")
        driver.execute_script("arguments[0].click();", button)
