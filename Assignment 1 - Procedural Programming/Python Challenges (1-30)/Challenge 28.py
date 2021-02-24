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
    print("Longest/Shortest/Amount [Lists] in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
    #just resetting the console colours
    print(Fore.RESET)
    #defining longest, shortest and count as longest name, shortest name and amount of names. After all is "calculated" we print them
    longest = max(names, key=len)
    shortest = min(names, key=len)
    count = len(names)
    print("Longest name:", longest)
    print("Shortest name:", shortest)
    print("Amount of names:", count)
    
#calling function so it actually runs    
process()

#while true asking if the user would like to exit (only yes as the user isn't inputting data)
while True:
     again = str(input(Fore.RESET + "\nWould you like to exit ["+Fore.GREEN+"Y"+Fore.RESET+"]: ")).lower()

     if again == "y":
           exit()

