#importing packages
import colorama
from colorama import Fore
import os
#clears the console screen
os.system("cls")
def process():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("ASCII values in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n", Fore.RESET)
    #asking the user their name
    name = input("What is your name? ")
    #defining "your_name" as the users input
    your_name = name
    #printing the ASCII values of the name (in a list format)
    print("ASCII Values: ", [ord(x) for x in your_name])
    
#calling function so it actually runs
process()


#while true loop to ask if the user wants to enter a different name. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to type a different name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()

