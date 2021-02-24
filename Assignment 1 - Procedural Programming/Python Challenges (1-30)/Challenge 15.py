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
            print("Username/Password Checker in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            #asks users input on the username (converts to lowercase to match variables)
            usernamein = input(Fore.RESET + "Input username: ").lower()
            #asks users input on the password (converts to lowercase to match variables)
            passwordin = input(Fore.RESET + "Input password: ").lower()
            #if the users input matches the variables it prints success then exits (like a login screen) and if one or none match then it prints failed
            if passwordin == password:
                if usernamein == username:
                         print(Fore.GREEN + "Success!")
                         time.sleep(1)
                         exit()
                else:
                    print(Fore.RED + "Failed!")
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