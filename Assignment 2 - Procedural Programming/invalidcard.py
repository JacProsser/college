import os
import colorama
from colorama import Fore, Back, Style
os.system("cls")
print("Loyalty Card Validation Checker in", Fore.YELLOW+"python", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
name = input("Enter your name: ")
postcode = input("Enter your postcode: ")
loyaltynum = input("Enter your loyalty card number: ")
loyaltyexpiry = input("Enter your loyalty card expiry date (MM/YY): ")

print(Fore.RED + "\nLoyalty Card Expired")
input()