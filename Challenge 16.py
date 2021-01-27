#importing packages
import os
import colorama
from colorama import Fore, Back, Style
import time

#list of star signs that can be used later on
starsign = ["Aquarius", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn","Pisces"]


def star():
            #clears the console screen
            os.system("cls")
            #printing "welcome message" saying what the program is and who it is made by
            print("Approx Star Sign in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            #asking the users birth month (converting that to lower to match if statements)
            month = input(Fore.RESET + "Enter Month [June, March, May]: ").lower()
            #if functions so if the users input is january it will output "Aprrox Star Sign: Aquarius" as that is first in the light "starsign[0]" and so on.
            if month == "january":
                print("Approx Star Sign:", starsign[0])
                
            elif month  == "february":
                print("Approx Star Sign:", starsign[11])
                
            elif month == "march":
                print("Approx Star Sign:", starsign[1])
                
            elif month == "april":
                print("Approx Star Sign:", starsign[2])
                
            elif month == "may":
                print("Approx Star Sign:", starsign[3])
                
            elif month == "june":
                print("Approx Star Sign:", starsign[4])
                
            elif month == "july":
                print("Approx Star Sign:", starsign[5])
                
            elif month == "august":
                print("Approx Star Sign:", starsign[6])
                
            elif month == "september":
                print("Approx Star Sign:", starsign[7])
                
            elif month == "october":
                print("Approx Star Sign:", starsign[8])
                
            elif month == "november":
                print("Approx Star Sign:", starsign[9])
                
            elif month == "december":
                print("Approx Star Sign:", starsign[10])
                
            else:
                print(Fore.RED + "Not a valid month!")

#calling function so it actually runs             
star()

#while true loop to ask if the user wants to enter another month. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another month? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          star()
    elif again == "n":
          exit()


