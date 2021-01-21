


import colorama
from colorama import Fore, Back, Style
import os

names = ["simon", "scott", "suzanne", "sam"]
def process():
    os.system("cls")
    print("Printing name from list in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser")
    print(Fore.RESET)
    print("Name:", names[2])

    
process()

while True:
     again = str(input(Fore.RESET + "\nWould you like to exit ["+Fore.GREEN+"Y"+Fore.RESET+"]: ")).lower()

     if again == "y":
           exit()
