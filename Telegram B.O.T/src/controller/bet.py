from src.controller.json import Json
import re


class Bet:

    def GetColor(Element):
        pattern = re.compile(r'alt="(.*?)"')
        match = pattern.search(Element)
        if match:
            return match.group(1)
        return ""

    def TrateMessage(Elements):
        new_element = Elements[-1]
        html_code = new_element.get_attribute("outerHTML")
        if html_code.find("<br>COR :"):
            info = html_code.split("<br>COR: ")[1].split("<br>")[0]
            Json.Save(Bet.GetColor(info))
            print('A bet message has been received')
            #\ud83d\udd34 VERMELHO