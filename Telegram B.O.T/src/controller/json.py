import json
import datetime

class Json:

    def Save(value):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        data = {"color": value, "time": date_time}
        with open("log/bets.json", "w", encoding='utf-8') as file:
            json.dump(data, file)
