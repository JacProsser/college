import os
import colorama
from colorama import Fore, Back, Style
import time


#set the password



def neg_pos():
#ask the user to input a password. u = user
            os.system("cls")
            print(Fore.GREEN+"Positive " + Fore.RESET+ "or" + Fore.RED + " negative " + Fore.RESET+ "in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            sum = float(input(Fore.RESET + "Input a number: "))

            if sum < 0:
                   print(Fore.RED + "Negative!")
            elif sum > 0:
                  print(Fore.GREEN + "Positive!")
            elif sum == 0:
                print("Neutral!")

neg_pos()

while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another number? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          neg_pos()
    elif again == "n":
          exit()


