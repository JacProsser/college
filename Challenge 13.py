#importing packages
import os
import colorama
from colorama import Fore, Back, Style
import time


#setting the password
password = "Jac"
#clears the console screen
os.system("cls")

def pwcheck():
#while true loop that asks the user for the password and if it is correct it prints success if it isn't correct then it prints failed and then clears the screen for the user to try again
       while True:
            
            print(Fore.RESET + "Password Checker in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            upassword = input(Fore.RESET + "Input a password: ")

            if upassword == password:
                   print(Fore.GREEN + "Success!")
                   break
            else:
                  print(Fore.RED + "Failed!")
                  #"sleeps" for 1 second
                  time.sleep(1)
                  #clears the console screen
                  os.system("cls")
                  
#calling function so it actually runs
pwcheck()




#makes user click enter before closing console
input() 