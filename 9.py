import colorama
from colorama import Fore
import os


os.system("cls")
def this():
     os.system("cls")
     print("Highest/Lowest ASCII value in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n", Fore.RESET)
     name = input("What is your name? ")
     your_name = name
     print("\nHighest ASCII value: ", [ord(x) for x in max(your_name)])
     print("Lowest ASCII value: ", [ord(x) for x in min(your_name)])
     print("Length of string: ", len(your_name))


this()

while True:
    again = str(input(Fore.RESET+"\nWould you like to type a different name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          this()
    elif again == "n":
          exit()

input()