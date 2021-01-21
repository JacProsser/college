import colorama
from colorama import Fore
import os

os.system("cls")
def process():
    os.system("cls")
    print("Sum of ASCII chars in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n", Fore.RESET)
    name = input("What is your name? ")
    your_name = name
    asciisum = sum([ord(x) for x in your_name])
    print("Sum of ASCII Chars:", asciisum)
    

process()

while True:
    again = str(input(Fore.RESET+"\nWould you like to type a different name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()

