#importing packages
import colorama
from colorama import Fore
import os

#defining speed function which will help us calculate the speed
def speed(distance, time):
    output = distance / time
    return  output

#clears the console screen    
os.system("cls")
def process():
    #clears the console screen
    os.system("cls")
    #printing "welcome message" saying what the program is and who it is made by
    print("Average Speed Calculator in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
    #asking for users input on distance (float)
    distance = float(input("Distance (M): "))
    #asking for users input on time (float)
    time = float(input("Time (s): "))
    #sum is equal to users input / users input (using the speed function)
    sum = speed(distance, time)
    #printing the end result
    print(sum, "M/S")

#calling the function so it actually runs
process()

#while true loop to ask if the user wants to enter another number. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to enter different values ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          exit()
