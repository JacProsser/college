#importing packages
import os
from colorama import Fore, Back, Style 
import time
import datetime




def calc():
    #clears the console screen
    os.system("cls")
    #just defining now using the dateime package (datetime.datetime.now() returns the time and date)
    now = datetime.datetime.now()
    #printing "welcome message" saying what the program is and who it is made by
    print("Basic Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
    #just resetting colours
    print(Fore.RESET)
    #printing asking what the user wants to do
    print("What do you want to do?\n\n", 
          Fore.GREEN+"(1) Add\n", 
          Fore.RED+"(2) Subtract\n", 
          Fore.YELLOW+"(3) Multiply\n", 
          Fore.BLUE+"(4) Divide\n", 
          Fore.WHITE+"(5) Exit\n\n", 
          
          Fore.RESET+"Copyright (c) Jac", now.year, "\n"
    )
#asking for users input which is named as choice
    choice = input("Choice: ")
#if choice is 1 then we add together both of the numbers that are inputted by the user
    if choice == "1":
        os.system("cls")
        print(Fore.GREEN + "Calculator [Addition]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)+float(num2)
        print("Answer: ", int(sum))
#if choice is 2 then we subtract together both of the numbers that are inputted by the user
    elif choice == "2":
        os.system("cls")
        print(Fore.RED + "Calculator [Subtraction]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)-float(num2)
        print("Answer: ", int(sum))
#if choice is 3 then we multiply together both of the numbers that are inputted by the user
    elif choice == "3":
        os.system("cls")
        print(Fore.YELLOW + "Calculator [Multiplication]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)*float(num2)
        print("Answer: ", int(sum))
#if choice is 4 then we divide  both of the numbers that are inputted by the user
    elif choice == "4":
        os.system("cls")
        print(Fore.BLUE + "Calculator [Division]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)/float(num2)
        print("Answer: ", sum)
#if choice is 5 then we exit the program
    elif choice == "5":
        exit()
#if input of "choice" is not valid we print invalid input then the program "sleeps" for 2 seconds then restarts
    else:
        print(Fore.RED+"Invalid input! Please choose from the options listed.")
        print(Fore.RESET)
        time.sleep(2)
        calc()


#calling function so it actually runs
calc()

#while true loop to ask if the user wants to use the calculator again. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to use the calculator again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          calc()
    elif again == "n":
          exit()