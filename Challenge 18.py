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
            print("Accurate Star Sign in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n")
            #asking the users birth day
            day = int(input(Fore.RESET + "Enter day [16, 2, 8]: "))
            #asking the users birth month (converting that to lower to match if statements)
            month = input(Fore.RESET + "Enter Month [June, March, May]: ").lower()
            #if functions so if the users input is january & the day is less than 20 it will output capricorn otherwise it will output aquarius and so on.
            if month == "january":
                starsignn = starsign[10] if (day < 20) else starsign[0]
                print("Star Sign:", starsignn)
                
            if month == "february":
                starsignn = starsign[0] if (day < 19) else starsign[11]
                print("Star Sign:", starsignn)
                
            if month == "march":
                starsignn = starsign[11] if (day < 21) else starsign[1]
                print("Star Sign:", starsignn)
                
            if month == "april":
                starsignn = starsign[1] if (day < 20) else starsign[2]
                print("Star Sign:", starsignn)
                
            if month == "may":
                starsignn = starsign[2] if (day < 21) else starsign[3]
                print("Star Sign:", starsignn)
                
            if month == "june":
                starsignn = starsign[3] if (day < 21) else starsign[4]
                print("Star Sign:", starsignn)
                
            if month == "july":
                starsignn = starsign[4] if (day < 23) else starsign[5]
                print("Star Sign:", starsignn)
                
            if month == "august":
                starsignn = starsign[5] if (day < 23) else starsign[6]
                print("Star Sign:", starsignn)
                
            if month == "september":
                starsignn = starsign[6] if (day < 23) else starsign[7]
                print("Star Sign:", starsignn)
                
            if month == "october":
                starsignn = starsign[7] if (day < 23) else starsign[8]
                print("Star Sign:", starsignn)
                
            if month == "november":
                starsignn = starsign[8] if (day < 22) else starsign[9]
                print("Star Sign:", starsignn)
                
            if month == "december":
                starsignn = starsign[9] if (day < 22) else starsign[10]
                print("Star Sign:", starsignn)

#calling function so it actually runs
star()


#while true loop to ask if the user wants to enter another month & day. if yes then it will restart the program. if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to enter another day & month? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          star()
    elif again == "n":
          exit()


