import colorama
from colorama import Fore
import os


pi = 3.14

def gardenarea(width, length):

    tgardenarea = width * length
    return tgardenarea

def bedarea(radius):

    tbedarea = pi * (radius * radius)
    return tbedarea

os.system("cls")
def process():
    os.system("cls")
    print("Turf Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET) 
    width = float(input("Width of Garden (M): "))
    length = float(input("Length of Garden (M): "))
    flower = float(input("Radius of Flower Bed (M): "))
    area1 = gardenarea(width, length)
    area2 = bedarea(flower)
    print("\nAmount of turf needed: ", area1 - area2)




process()

while True:
    again = str(input(Fore.RESET+"\nWould you like to enter different values ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()