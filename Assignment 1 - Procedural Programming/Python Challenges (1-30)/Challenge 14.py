#importing packages
import os
import colorama
from colorama import Fore, Back, Style
import time


def neg_pos():
#clears the console screen      
            os.system("cls")
            #printing "welcome message" saying what the program is and who it is made by
            print(Fore.GREEN+"Positive " + Fore.RESET+ "or" + Fore.RED + " negative " + Fore.RESET+ "in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            #asking user to input a number (as float)
            sum = float(input(Fore.RESET + "Input a number: "))
            #if the number is less than 0 then it prints negative. if it is greater than 0 it prints positive. if it is 0 then it print neutral
            if sum < 0:
                   print(Fore.RED + "Negative!")
            elif sum > 0:
                  print(Fore.GREEN + "Positive!")
            elif sum == 0:
                print("Neutral!")
                
#calling function so it actually runs
neg_pos()

#while true loop to ask if the user wants to enter another number. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another number? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          neg_pos()
    elif again == "n":
          exit()


