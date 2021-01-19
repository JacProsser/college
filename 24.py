
import colorama
from colorama import Fore, Back, Style
import os







def calc():
    os.system("cls")
    print("Basic Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
    num1 = float(input("Enter a number: "))
    print(Fore.RESET)
    print("What do you want to do?\n\n", Fore.GREEN+"(1) Inches to Centimetres\n", Fore.RED+"(2) Centimetres to Inches\n", Fore.WHITE+"(3) Exit\n\n", Fore.RESET+"Copyright (c) Jac 2021\n"
    )

    choice = input("Choice: ")

    if choice == "1":
        os.system("cls")
        print(Fore.GREEN + "Inches to Centimetres\n")
        sum = num1 * 2.54
        print("Answer: ", round(sum, 2), "cm", sep="")

    elif choice == "2":
        os.system("cls")
        print(Fore.RED + "Centimetres to Inches\n")
        sum = num1 / 2.54
        print("Answer: ", round(sum, 2), "in", sep="")

    elif choice == "3":
     exit()





calc()

while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another number? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          calc()
    elif again == "n":
          exit()

