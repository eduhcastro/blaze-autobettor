from os import system, name
from pyfiglet import Figlet
from termcolor import colored

import sys


class System:

    def CleanConsole():
        system('cls' if name == 'nt' else 'clear')

    def SetTitle():
        system('title Blaze Double Bot')

    def HandleInterrupt(signal, frame):
        print('\n Leaving...')
        sys.exit(0)
        
    def SetInterface():
      f = Figlet(font='isometric4')
      print(colored(f.renderText("BDB"), 'light_red'))
      print(colored("Blaze Double Bot - 0.1", 'white'))
      print(colored("Developed by: CastroMS | 2023 | It must not be shared.", 'light_red'))
      print(colored("Please wait while the page loads", 'light_red'))

