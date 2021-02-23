#asking user what their name is
name = input("What is your name? ")
#defining that "your_name" = the users input
your_name = name
#printing hello with the users name
print("Hello", your_name)
#printing the memory location of the users input
print("Memory Location: ", id(your_name))
#gets user to press enter before closing console (get time to read it instead of closing after print)
input()
