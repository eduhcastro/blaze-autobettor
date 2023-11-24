import os
import time
import json
from src.controller.bet import Bet

class Watch:

    def Bets(driver):
        initial_timestamp = os.stat("../Telegram B.O.T/log/bets.json").st_mtime
        while True:
            time.sleep(1)
            current_timestamp = os.stat(
                "../Telegram B.O.T/log/bets.json").st_mtime
            if current_timestamp != initial_timestamp:
                print("New bet received")
                Bet.SetValue(driver)
                Bet.ClickColor(driver)
                Bet.Handler(driver)
                initial_timestamp = current_timestamp
