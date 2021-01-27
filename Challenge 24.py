#importing packages
import colorama
from colorama import Fore, Back, Style
import os

#defining function inches to centimetres
def InToCm(x):
   return x * 2.54
#defining function centimetres
def CmtoIn(x):
    return x / 2.54


def calc():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("In/Cm Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
    #asking a user for a number (float)
    num1 = float(input("Enter a number: "))
    #resetting console colours
    print(Fore.RESET)
    #printing asking the user what they would like to do
    print("What do you want to do?\n\n", Fore.GREEN+"(1) Inches to Centimetres\n", Fore.RED+"(2) Centimetres to Inches\n", Fore.WHITE+"(3) Exit\n\n", Fore.RESET+"Copyright (c) Jac 2021\n"
    )
#asking users choice 
    choice = input("Choice: ")
#if choice is 1 then the calculator does the inches to centimetres option. if choice is 2 then calcultor does centimetres to inches option. and if choice 3 the program exits
    if choice == "1":
        os.system("cls")
        print(Fore.GREEN + "Inches to Centimetres\n")
        sum = InToCm(num1)
        print("Answer: ", round(sum, 2), "cm", sep="")

    elif choice == "2":
        os.system("cls")
        print(Fore.RED + "Centimetres to Inches\n")
        sum = CmtoIn(num1)
        print("Answer: ", round(sum, 2), "in", sep="")

    elif choice == "3":
     exit()




#calling function so it actually runs
calc()

#while true loop to ask if the user wants to enter another number. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another number? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          calc()
    elif again == "n":
          exit()

