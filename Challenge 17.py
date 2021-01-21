import os
import colorama
from colorama import Fore, Back, Style
import time



username = "college"
password = "merthyr"


def passw():
#ask the user to input a password. u = user
            os.system("cls")
            print("Username/Password Checker using complex boolean expressions in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            usernamein = input(Fore.RESET + "Input username: ").lower()
            passwordin = input(Fore.RESET + "Input password: ").lower()
            if username == usernamein and password == passwordin:
                print(Fore.GREEN + "Success!")
            else:
                print(Fore.RED + "Failed!")
                
                
            




passw()

while True:
    again = str(input(Fore.RESET+"\nWould you like to try again! ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          passw()
    elif again == "n":
          exit()