import os
import colorama
from colorama import Fore, Back, Style




os.system("cls")
print("Loyalty Card Validation Checker in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
name = input("Enter your name: ")
postcode = input("Enter your postcode: ")
loyaltynum = int(input("Enter your loyalty card number (Located on the front): "))
loyaltyexpiry = input("Enter your loyalty card expiry date (MM/YY): ")
print(Fore.RED + "\nInvalid Name")
print(Fore.RED + "\nInvalid Postcode")
if loyaltynum == 10:
    print(Fore.GREEN + "\nLoyalty Card Valid")
else:
    print(Fore.RED + "\nLoyalty Card Expired")

input()