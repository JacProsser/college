
import colorama
from colorama import Fore, Back, Style
import os

names = ["simon", "scott", "suzanne", "sam"]
def process():
    os.system("cls")
    print("Longest/Shortest/Amount [Lists] in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
    print(Fore.RESET)
    longest = max(names, key=len)
    shortest = min(names, key=len)
    count = len(names)
    print("Longest name:", longest)
    print("Shortest name:", shortest)
    print("Amount of names:", count)
    
    
process()

while True:
     again = str(input(Fore.RESET + "\nWould you like to exit ["+Fore.GREEN+"Y"+Fore.RESET+"]: ")).lower()

     if again == "y":
           exit()

