#importing packages
import os
import colorama
from colorama import Fore, Back, Style
import time


#sets the username
username = "college"
#sets the password
password = "merthyr"


def passw():
            #clears the console screen
            os.system("cls")
            #printing "welcome message" saying what the program is and who it is made by
            print("Username/Password Checker using complex boolean expressions in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            #asking user to input username
            usernamein = input(Fore.RESET + "Input username: ")
            #asking user to input password
            passwordin = input(Fore.RESET + "Input password: ")
            """
            if statement using complex boolean expressions that state if the username is equal to the input and the password is equal to the user input then we print success however
            if none of them are right then it prints failed
            """
            if username == usernamein and password == passwordin:
                print(Fore.GREEN + "Success!")
                #"sleeps" for 1 second
                time.sleep(1)
                #exits program
                exit()
            else:
                print(Fore.RED + "Failed!")
                
                
            



#calling function so it actually runs
passw()
#while true loop to ask if the user wants to try again if yes then it will restart the program. (doesn't show if you get it correct as the program exits) if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to try again! ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          passw()
    elif again == "n":
          exit()