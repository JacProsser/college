#importing packages
import colorama
from colorama import Fore, Back, Style
import os

#list of names
names = ["simon", "scott", "suzanne", "sam"]
def process():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("Printing name from list in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser")
    #just restting console colours
    print(Fore.RESET)
    #printing the 2 name in the list
    print("Name:", names[2])

#calling the function so it actually runs    
process()

#while true asking if the user would like to exit (only yes as the user isn't inputting data)
while True:
     again = str(input(Fore.RESET + "\nWould you like to exit ["+Fore.GREEN+"Y"+Fore.RESET+"]: ")).lower()

     if again == "y":
           exit()
