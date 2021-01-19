
import os 
import colorama
from colorama import Fore
import time



x = 0
score = x
lst2 = []
realnames = ["melaniebrown", "melaniechisholm", "emmabunton", "gerihalliwell", "victoriabeckham"] 


os.system("cls")
def spice():
       os.system("cls")
       print("Spice Girls [Challenge] in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
       print("These are the nicknames/stage names for the SPICE GIRLS! | Do you know all of their real names?")
       print("\nNicknames: Scary Spice, Sporty Spice, Baby Spice, Ginger Spice and Posh Spice")
       lst2 = [item for item in input("\nEnter real names of the spice girls. e.g. firstnamelastname firstnamelastname: ").split()] 

       if all(item in realnames for item in lst2):
           print(Fore.GREEN+"Viva Forever!")
           time.sleep(1)
           exit()
       else:
           print(Fore.RED+"Who do you think you are?")
       input()
           


    







spice()

while True:
    again = str(input(Fore.RESET+"\nWould you like to try again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          spice()
    elif again == "n":
          exit()



input()