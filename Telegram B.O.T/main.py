import signal
from termcolor import colored

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from src.controller.system import System
from src.web.chrome import Chrome

# Get signal to exit script
signal.signal(signal.SIGINT, System.HandleInterrupt)

System.CleanConsole()
System.SetTitle()
System.SetInterface()
driver = Chrome.Driver()


driver.get("https://web.telegram.org/z/#-1717496704")
#search_field = driver.find_element(By.ID, "search_form_input_homepage")

user_input = input(colored("Enter the word (Done) when ready: ", 'light_blue'))

if user_input == "done":
    print("Monitoring started")
    Chrome.Watch(driver)

## Monitora as alterações no campo de pesquisa
#current_value = search_field.get_attribute("value")
#while True:
#    new_value = search_field.get_attribute("value")
#    if current_value != new_value:
#        print("Campo de pesquisa foi alterado!")
#        current_value = new_value
#
