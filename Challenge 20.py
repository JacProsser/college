import os
import colorama 
from colorama import Fore, Back, Style 
import sys
import time
import pygame


def music():
    pygame.init()
    pygame.mixer.music.load("C:\\Users\\Jac\\Music\\Unfold (Slowed).mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

def calc():
    os.system("cls")
    print("Basic Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
    print(Fore.RESET)
    print("What do you want to do?\n\n", Fore.GREEN+"(1) Add\n", Fore.RED+"(2) Subtract\n", Fore.YELLOW+"(3) Multiply\n", Fore.BLUE+"(4) Divide\n", Fore.WHITE+"(5) Exit\n\n", Fore.RESET+"Copyright (c) Jac 2021\n"
    )

    choice = input("Choice: ")

    if choice == "1":
        os.system("cls")
        print(Fore.GREEN + "Calculator [Addition]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)+float(num2)
        print("Answer: ", int(sum))

    elif choice == "2":
        os.system("cls")
        print(Fore.RED + "Calculator [Subtraction]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)-float(num2)
        print("Answer: ", int(sum))

    elif choice == "3":
        os.system("cls")
        print(Fore.YELLOW + "Calculator [Multiplication]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)*float(num2)
        print("Answer: ", int(sum))

    elif choice == "4":
        os.system("cls")
        print(Fore.BLUE + "Calculator [Division]\n")
        num1 = input("Please enter your 1st number: ")
        num2 = input("Please enter your 2nd number: ")
        sum = float(num1)/float(num2)
        print("Answer: ", sum)
    elif choice == "5":
        sys.exit()

    else:
        print(Fore.RED+"Invalid input! Please choose from the options listed.")
        print(Fore.RESET)
        time.sleep(2)
        calc()


music()
calc()
while True:
    again = str(input(Fore.RESET+"\nWould you like to use the calculator again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          calc()
    elif again == "n":
          sys.exit()