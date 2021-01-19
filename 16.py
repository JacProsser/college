import os
import colorama
from colorama import Fore, Back, Style
import time


starsign = ["Aquarius", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn","Pisces"]


def star():
            os.system("cls")
            print("Approx Star Sign in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            month = input(Fore.RESET + "Enter Month [June, March, May]: ").lower()
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
                
star()

while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another month? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          star()
    elif again == "n":
          exit()


