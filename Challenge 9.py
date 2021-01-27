#importing packages
import colorama
from colorama import Fore
import os

#clears the console screen
os.system("cls")
def this():
     #clears the console screen
     os.system("cls")
     #printing "welcome message" saying what the program is and who it is made by
     print("Highest/Lowest ASCII value in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n", Fore.RESET)
     #asking what the users name is
     name = input("What is your name? ")
     #defining "your_name" as the users input
     your_name = name
     #prints the highest ascii value within the name
     print("\nHighest ASCII value: ", [ord(x) for x in max(your_name)])
     #prints the lowest ascii value within the name
     print("Lowest ASCII value: ", [ord(x) for x in min(your_name)])
     #prints the length of the name
     print("Length of string: ", len(your_name))

#calling function so it actually runs
this()


#while true loop to ask if the user wants to enter a different name. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to type a different name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          this()
    elif again == "n":
          exit()

