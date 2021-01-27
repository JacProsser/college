#importing packages
import colorama
from colorama import Fore, Back, Style
import os

#list of names
names = ["simon", "scott", "suzanne", "sam", "jac", "lucy", "rubi", "cheyane", "nicola", "colin", "issac"]

def process():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("Name Finder in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
    #restting console colours
    print(Fore.RESET)
    #getting users input and converting to lower to match the list
    nameinput = input("Type a name: ").lower()
#if statement that checks the input. and if the input is found within the list it prints name found otherwise it prints name not found.
    if nameinput in names:
         print(Fore.GREEN + "Name Found!")
    else:
         print(Fore.RED + "Name not found!")

#calling function
process()

#while true loop to ask if the user wants to take the quiz again. if yes then it will restart the program. if no it will exit the console
while True:
     again = str(input(Fore.RESET + "\nWould you like to enter another name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()

     if again == "y":
           process()
     elif again == "n":
           exit()


