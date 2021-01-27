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

#clears the console screen
os.system("cls")
def process():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("Turf Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET) 
    #asking users input on width of garden (float)
    width = float(input("Width of Garden (M): "))
    #asking users input on length of garden (float)
    length = float(input("Length of Garden (M): "))
    #asking users input on radius of flower bed (float)
    flower = float(input("Radius of Flower Bed (M): "))
    #using function garden area to workout "area1"
    area1 = gardenarea(width, length)
    #using function bed area to workout "area2"
    area2 = bedarea(flower)
    #printing end result
    print("\nAmount of turf needed: ", area1 - area2)



#calling function so it actually runs
process()

#while true loop to ask if the user wants to enter another number. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to enter different values ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()