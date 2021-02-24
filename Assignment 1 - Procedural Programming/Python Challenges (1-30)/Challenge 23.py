#importing packages
import colorama
from colorama import Fore, Back, Style
import os

#clears the console screen
os.system("cls")
#defining answer as tomorrow
answer = "tomorrow"
#while true loop that keeps asking question and when it is correct it prints well done and then breaks otherwise it prints wrong try again
while True:
    question = input("\nWhat is always coming, but never arrives? ").lower()
    if question == answer:
        print (Fore.GREEN + "Well done!", Fore.RESET)
        break
    else:
        print(Fore.RED + "Wrong try again!", Fore.RESET)

#input so user can see all outputs
input()