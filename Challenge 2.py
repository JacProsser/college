#tells the user what to do
print('Please input 2 different numbers. [Average Calculator]')
#waits for users input on number 1
num1 = float(input("Number 1: ") )
#waits for users input on number 2
num2 = float(input("Number 2: ") )
#calculates the average
sum = (num1 + num2)/2
#shows/prints the average on the screen
print ("Average: ", int(sum))
#makes sure the user clicks enter before the "console" closes. this allows them to see the answer instead of the console closing instantly
input()