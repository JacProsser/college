import datetime
name = input("What is your name? ")
year = int(input("What year were you born? "))
subject = input("What is your favourite subject? ").lower()
thisyear = datetime.datetime.now().year
age = thisyear - year
print("I love " + subject + " and i am " + str(age) + " years old "+ "too!")
input()