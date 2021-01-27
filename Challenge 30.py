#importing packages
import os 
import colorama
from colorama import Fore

#clears the console screen
os.system("cls")
def listing():
       #clears the console screen
       os.system("cls")
       #printing "welcome message" saying what the program is and who it is made by
       print("Number Sorter [Ascending] in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
       #getting list as input
       a = list(map(int,input("\nEnter 10 numbers e.g. 20 40 56:\n").split()))
       #sort list
       a.sort()
       #print sorted list
       print("\nSorted list:\n" + ', '.join(map(str, a)))

#calling the function so it actually runs
listing()

#while true loop asking if the user would like to sort more numbers. if yes then it will restart the program if no then it will exit the program.
while True:
    again = str(input(Fore.RESET+"\nWould you like to sort more numbers ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          listing()
    elif again == "n":
          exit()
