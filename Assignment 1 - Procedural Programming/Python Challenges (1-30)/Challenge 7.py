#importing packages
import colorama
from colorama import Fore
import os
#clears the console screen
os.system("cls")
def process():
    #clears the console screen
    os.system("cls")
    #asking what users name is
    name = input("What is your name? ")
    #defining that "your_name" = users input (name)
    your_name = name
    #printing the name backwards. e.g jac to caj
    print("Name backwards: ", your_name[::-1])
    #printing the name 1000 times
    print("Name printed 1000 times: ", your_name * 1000)


#calling function so it actually runs
process()

#while true loop to ask if the user wants to enter a different name. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to type a different name? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()

