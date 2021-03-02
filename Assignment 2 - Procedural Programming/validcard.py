import os
import colorama
from colorama import Fore, Back, Style
os.system("cls")
print(Fore.RED + """
.            . ,       __         .  .  .   .   .    ,           __ .        .        
|    _   . _.|-+-  .  /  ` _.._. _|  \  / _.|* _| _.-+-* _ ._   /  `|_  _  _.;_/ _ ._.
|___(_)\_|(_]| | \_|  \__.(_][  (_]   \/ (_]||(_](_] | |(_)[ )  \__.[ )(/,(_.| \(/,[  
       ._|       ._|     
                                                                                                                                      
      """ + Fore.RESET)

name = input("Enter your name: ")
postcode = input("Enter your postcode: ")
loyaltynum = input("Enter your loyalty card number: ")
loyaltyexpiry = input("Enter your loyalty card expiry date (MM/YY): ")

print(Fore.GREEN + "\nLoyalty Card Valid")
input()