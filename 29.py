names = ["simon", "scott", "suzanne", "sam"]
import colorama
from colorama import Fore, Back, Style
import os

def process():
    os.system("cls")
    print("Name Finder in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
    print(Fore.RESET)
    nameinput = input("Type a name: ").lower()

    if nameinput in names:
         print(Fore.GREEN + "Name Found!")
    else:
         print(Fore.RED + "Name not found!")

process()

while True:
     again = str(input(Fore.RESET + "\nWould you like to enter another name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()

     if again == "y":
           process()
     elif again == "n":
           exit()


