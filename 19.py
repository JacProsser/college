
import os 
import colorama
from colorama import Fore
import time




realnames = ["melanie brown", "melanie chisholm", "emma bunton", "geri halliwell", "victoria beckham"] 


os.system("cls")
def spice():
       os.system("cls")
       print("Spice Girls [Challenge] in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
       print("These are the nicknames/stage names for the SPICE GIRLS! | Do you know all of their real names?")
       print("\nNicknames: Scary Spice, Sporty Spice, Baby Spice, Ginger Spice and Posh Spice")
       scary_spice = input("\nWhat is Scary Spice's name? ")
       sporty_spice = input("\nWhat is Sporty Spice's name? ")
       baby_spice = input("\nWhat is Baby Spice's name? ")
       ginger_spice = input("\nWhat is Ginger Spice's name? ")
       posh_spice = input("\nWhat is Posh Spice's name? ")
       
       if scary_spice == realnames[0] and sporty_spice == realnames[1] and baby_spice == realnames[2] and ginger_spice == realnames[3] and posh_spice == realnames[4]:
           print(Fore.GREEN + "\nViva Forever!")
           time.sleep(2)
           exit()
       else:
           print(Fore.RED + "Who do you think you are?")
       
  

           





spice()

while True:
    again = str(input(Fore.RESET+"\nWould you like to try again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          spice()
    elif again == "n":
          exit()



