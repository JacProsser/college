#asks the user for total cost of sweets. float meaning that it can only be a float value
totalcost = float(input("Total cost of sweets (£): "))
#asks the user for amount of money given. float meaning that it can only be a float value
totalmoney = float(input("Amount of money given (£): "))
#takes amount of money given and subtracts the cost of sweets
sum = totalmoney - totalcost
#times the amount left by 100 to give change in pence
changeinpence = sum * 100
#prints change in pence. "sep=''" meaning seperator allowing me to put the "p" next to the amount e.g. 500p
print("Change: ", int(changeinpence),"p", sep='')
#makes sure the user clicks enter before the "console" closes. this allows them to see the answer instead of the console closing instantly
input()