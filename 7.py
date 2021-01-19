import colorama
from colorama import Fore
import os

os.system("cls")
def process():
    os.system("cls")
    name = input("What is your name? ")
    your_name = name
    print("Name backwards: ", your_name[::-1])
    print("Name printed 1000 times: ", your_name * 1000)

process()

while True:
    again = str(input(Fore.RESET+"\nWould you like to type a different name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()

