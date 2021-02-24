#importing packages
import colorama
from colorama import Fore
import os


def quiz():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("Literacy Quiz in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n", Fore.RESET)
    #while true loop that keeps asking for the users input until it matches the answers within a1
    while True:
       q1 = input("\n1. What comes after the end of a sentence? ").lower()
       a1 = ["full stop", "."]
       if q1 in a1:
          print(Fore.GREEN + "Well Done!" + Fore.RESET)
          break
       else:
          print(Fore.RED + "Try Again!" + Fore.RESET)
    #while true loop that keeps asking for the users input until it matches the answers within a2
    while True:
        q2 = input("\n2. Give me an example of an uppercase letter? ")
        a2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        if q2 in a2:
            print(Fore.GREEN + "Well Done!" + Fore.RESET)
            break
        else:
            print( Fore.RED + "Try Again!" + Fore.RESET)
    #while true loop that keeps asking for the users input until it matches the answers within a3
    while True:
        q3 = input("\n3. Why do we use commas? ").lower()
        a3 = "separate"
        printing = q3.split()
        if a3 in printing:
            print(Fore.GREEN + "Well Done!" + Fore.RESET)
            break
        else:
            print(Fore.RED + "Try Again!" + Fore.RESET)


#calling function so it actually runs
quiz()

#while true loop to ask if the user wants to take the quiz again. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to take the quiz again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          quiz()
    elif again == "n":
          exit()

