#just import date package 
import datetime
#asking user for name
name = input("What is your name? ")
#asking user for the year that they were born (as int)
year = int(input("What year were you born? "))
#asking user what their favourite subject is (conveting it to lowercase as it is in a sentence and wouldn't make sense with a capital mid way through)
subject = input("What is your favourite subject? ").lower()
#just defining that "thisyear" = "2021"
thisyear = datetime.datetime.now().year
#defining that age is equal to thisyear - what year they were born
age = thisyear - year
#printing the sentence with the user inputs included 
print("I love " + subject + " and i am " + str(age) + " years old "+ "too!")
#gets user to press enter before closing console (get time to read it instead of closing after print)
input()