import colorama
from colorama import Fore
import os

os.system("cls")
def process():
    os.system("cls")
    distanceM = float(input("Distance (m): "))
    timeS = float(input("Time (s): "))


process()

while True:
    again = str(input(Fore.RESET+"\nWould you like to enter different values ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()
