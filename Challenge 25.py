import colorama
from colorama import Fore
import os

def speed(distance, time):
    output = distance / time
    return  output
    
os.system("cls")
def process():
    os.system("cls")
    print("Average Speed Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
    distance = float(input("Distance (M): "))
    time = float(input("Time (s): "))
    sum = speed(distance, time)
    
    print(sum, "M/S")


process()

while True:
    again = str(input(Fore.RESET+"\nWould you like to enter different values ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()
