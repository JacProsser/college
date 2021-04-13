import os
import colorama
from datetime import datetime, date
from colorama import Fore, Back, Style
import time
import ctypes


ctypes.windll.kernel32.SetConsoleTitleW("Loyalty Card Validation Checker | Made by Jac Prosser")
def process():
    os.system("cls")
    print(Fore.RED + """
  _                      _ _            ____              _    ____ _               _             
 | |    ___  _   _  __ _| | |_ _   _   / ___|__ _ _ __ __| |  / ___| |__   ___  ___| | _____ _ __ 
 | |   / _ \| | | |/ _` | | __| | | | | |   / _` | '__/ _` | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| (_) | |_| | (_| | | |_| |_| | | |__| (_| | | | (_| | | |___| | | |  __/ (__|   <  __/ |   
 |_____\___/ \__, |\__,_|_|\__|\__, |  \____\__,_|_|  \__,_|  \____|_| |_|\___|\___|_|\_\___|_|   
             |___/             |___/                                                              
                                                                                                        
      """ + Fore.RESET)
    print(Fore.YELLOW + "Welcome to the Loyalty Card Validation Checker!" + Fore.RESET)
    confirmation1 = input(Fore.YELLOW + "To begin the process please click enter." + Fore.RESET)
    
    os.system("cls")
    print(Fore.RED + """
  _                      _ _            ____              _    ____ _               _             
 | |    ___  _   _  __ _| | |_ _   _   / ___|__ _ _ __ __| |  / ___| |__   ___  ___| | _____ _ __ 
 | |   / _ \| | | |/ _` | | __| | | | | |   / _` | '__/ _` | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| (_) | |_| | (_| | | |_| |_| | | |__| (_| | | | (_| | | |___| | | |  __/ (__|   <  __/ |   
 |_____\___/ \__, |\__,_|_|\__|\__, |  \____\__,_|_|  \__,_|  \____|_| |_|\___|\___|_|\_\___|_|   
             |___/             |___/                                                              
                                                                                                               
      """ + Fore.RESET)
    while True:
        name = input("Enter your name: ")
        if not name.isalpha():
         print("Name can not contain numbers.")
        else:
            break
 
    valid1 = False
    while valid1 == False:
        postcode = input("Enter your postcode e.g. CF47 9RD: ")
        if len(postcode) >= 7:
            valid1 = True
        else:
            valid1 = False
    #loyaltynum = input("Enter your loyalty card number (Located on the front): ")
    valid2 = False
    while valid2 == False:
       loyaltynum = input("Enter your loyalty card number (Located on the front): ")
       if len(loyaltynum) == 8:
          valid2 = True
          try:
             type = float(loyaltynum)
          except:
             print("Invalid card number. (make sure number doesn't include any characters)")
             valid2 = False
       else:
             valid2 = False
             
    now = datetime.now()
    now = date(year=now.year, month=now.month, day=1)

    loyalty_expiry = input("Enter your loyalty card expiry date (MM/YY): ")
    expiry = datetime.strptime(loyalty_expiry, "%m/%y")
    expiry = date(year=expiry.year, month=expiry.month, day=1)
    
    print("\n")
    import sys
    for remaining in range(5, -1, -1):
          sys.stdout.write("\r")
          sys.stdout.write("Checking card... | Time Remaining {}s".format(remaining))
          sys.stdout.flush()
          time.sleep(1)
          
    print("\n")
    if now == expiry:
        print(Fore.RED + "\nLoyalty Card Expired")
    elif now > expiry:
        print(Fore.RED + "\nLoyalty Card Expired")
    elif now < expiry:
        digitcheck = int(loyaltynum[7])
        reverse = loyaltynum[6] + loyaltynum[5] + loyaltynum[4] + loyaltynum[3] + loyaltynum[2] + loyaltynum[1] + loyaltynum[0]
        num1 = reverse[0]
        num3 = reverse[2]
        num5 = reverse[4]
        num7 = reverse[6]
        
        num1 = int(reverse[0]) * 2
        num3 = int(reverse[2]) * 2
        num5 = int(reverse[4]) * 2
        num7 = int(reverse[6]) * 2
        if num1 > 9:
          num1 = num1 - 9
          
        if num3 > 9:
          num3 = num3 - 9
        if num5 > 9:
          num5 = num5 - 9
        if num7 > 9:
          num7 = num7 - 9
          
        overall = num1 + int(reverse[1]) + num3 + int(reverse[3]) + num5 + int(reverse[5]) + num7
        overall = overall + digitcheck
        

        print("\n")        
        if overall % 10 == 0:
           print(Fore.GREEN + "\nLoyalty Card Valid")
        else:
           print(Fore.RED + "\nLoyalty Card Invalid")    
	        

    #validation

"""   
print(Fore.RED + "\nInvalid Name")
print(Fore.RED + "\nInvalid Postcode")
print(Fore.RED + "\nLoyalty Card Expired")
"""

process()

while True:
    again = str(input(Fore.RESET+"\nWould you like to check another card? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          process()
    elif again == "n":
          os.system('cls')
          print(Fore.RED + """
  _                      _ _            ____              _    ____ _               _             
 | |    ___  _   _  __ _| | |_ _   _   / ___|__ _ _ __ __| |  / ___| |__   ___  ___| | _____ _ __ 
 | |   / _ \| | | |/ _` | | __| | | | | |   / _` | '__/ _` | | |   | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| (_) | |_| | (_| | | |_| |_| | | |__| (_| | | | (_| | | |___| | | |  __/ (__|   <  __/ |   
 |_____\___/ \__, |\__,_|_|\__|\__, |  \____\__,_|_|  \__,_|  \____|_| |_|\___|\___|_|\_\___|_|   
             |___/             |___/                                                              

                """ + Fore.RESET)
          print("\nThank you for using the \"Loyalty Card Validation Checker\"")
          time.sleep(2)
          exit()
