#importing packages
import os 
import colorama
from colorama import Fore
import time

#list of the "answers"
realnames = ["melanie brown", "melanie chisholm", "emma bunton", "geri halliwell", "victoria beckham"] 

#clears the console screen
os.system("cls")
def spice():
       #clears the console screen
       os.system("cls")
       #printing "welcome message" saying what the program is and who it is made by
       print("Spice Girls [Challenge] in",  Fore.YELLOW+"python.", Fore.RESET+"| Made by", Fore.CYAN+"Jac Prosser\n" + Fore.RESET)
       #printing what we need the user to do
       print("These are the nicknames/stage names for the SPICE GIRLS! | Do you know all of their real names?")
       #printing nicknames of spice girls
       print("Nicknames: Scary Spice, Sporty Spice, Baby Spice, Ginger Spice and Posh Spice")
       #asking for users input on name (converted to lowercase to match list)
       scary_spice = input("\nWhat is Scary Spice's name? ").lower()
       #asking for users input on name (converted to lowercase to match list)
       sporty_spice = input("\nWhat is Sporty Spice's name? ").lower()
       #asking for users input on name (converted to lowercase to match list)
       baby_spice = input("\nWhat is Baby Spice's name? ").lower()
       #asking for users input on name (converted to lowercase to match list)
       ginger_spice = input("\nWhat is Ginger Spice's name? ").lower()
       #asking for users input on name (converted to lowercase to match list)
       posh_spice = input("\nWhat is Posh Spice's name? ").lower()
       #if all of the user inputs match the whole list then it prints viva forever. if all of the user inputs or some of them are wrong it prints who do you think you are
       if scary_spice == realnames[0] and sporty_spice == realnames[1] and baby_spice == realnames[2] and ginger_spice == realnames[3] and posh_spice == realnames[4]:
           print(Fore.GREEN + "\nViva Forever!")
           #"sleep" for 2 seconds then exit
           time.sleep(2)
           exit()
       else:
           print(Fore.RED + "Who do you think you are?")
       
#calling function so it actually runs
spice()
#while true loop to ask if the user wants to try again if yes then it will restart the program. (doesn't show if you get it correct as the program exits) if no it will exit the console
while True:
    again = str(input(Fore.RESET+"\nWould you like to try again? ["+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"N"+ Fore.RESET+"]: ")).lower()
    if again == "y":
          print(Fore.RESET)
          spice()
    elif again == "n":
          exit()



