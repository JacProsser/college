import os
import colorama
from colorama import Fore, Back, Style
import time


#set the password
password = "Jac"
os.system("cls")

def pwcheck():
#ask the user to input a password. u = user
       while True:
            
            print(Fore.RESET + "Password Checker in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            upassword = input(Fore.RESET + "Input a password: ")

            if upassword == password:
                   print(Fore.GREEN + "Success!")
                   break
            else:
                  print(Fore.RED + "Failed!")
                  time.sleep(1)
                  os.system("cls")

pwcheck()





input() 