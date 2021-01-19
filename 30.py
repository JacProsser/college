import os 
import colorama
from colorama import Fore

os.system("cls")
def listing():
       os.system("cls")
       print("Number Sorter [Ascending] in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
       a = list(map(int,input("\nEnter 10 numbers e.g. 20 40 56:\n").split()))

       a.sort()
       print("\nSorted list:\n" + ', '.join(map(str, a)))


listing()

while True:
    again = str(input(Fore.RESET+"\nWould you like to sort more numbers ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          listing()
    elif again == "n":
          exit()
