import signal
from termcolor import colored

from src.controller.system import System
from src.web.chrome import Chrome
from src.controller.watch import Watch

# Get signal to exit script
signal.signal(signal.SIGINT, System.HandleInterrupt)

System.CleanConsole()
System.SetTitle()
System.SetInterface()
driver = Chrome.Driver()


driver.get("https://blaze.com/r/nP9ApZ")
#search_field = driver.find_element(By.ID, "search_form_input_homepage")

user_input = input(colored("Enter the word (Done) when ready: ", 'light_red'))

if user_input == "done":
  
    print("Monitoring started")
    Chrome.Watch(driver)
    Watch.Bets(driver)