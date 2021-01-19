import colorama
from colorama import Fore
import os


def quiz():
    os.system("cls")
    print("Literacy Quiz in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n", Fore.RESET)
    while True:
       q1 = input("\n1. What comes after the end of a sentence? ").lower()
       a1 = ["full stop", "."]
       if q1 in a1:
          print("Well Done!")
          break
       else:
          print("Try Again!")
    while True:
        q2 = input("\n2. Give me an example of an uppercase letter? ")
        a2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        if q2 in a2:
            print("Well Done!")
            break
        else:
            print("Try Again!")
    while True:
        q2 = input("\n3. Why do we use commas? ").lower()
        a2 = "separate"
        printing = q2.split()
        if a2 in printing:
            print("Well Done!")
            break
        else:
            print("Try Again!")



quiz()

while True:
    again = str(input(Fore.RESET+"\nWould you like to take the quiz again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          quiz()
    elif again == "n":
          exit()

