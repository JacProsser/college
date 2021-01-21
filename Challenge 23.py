import colorama
from colorama import Fore, Back, Style
import os

os.system("cls")
answer = "tomorrow"

while True:
    question = input("\nWhat is always coming, but never arrives? ").lower()
    if question == answer:
        print (Fore.GREEN + "Well done!", Fore.RESET)
        break
    else:
        print(Fore.RED + "Wrong try again!", Fore.RESET)

input()