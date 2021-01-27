print("Area of rectangle [Calculator]\n")
#asks the user what the width of the rectangle is. (float)
width = float(input("Width: "))
#asks the user what the height of the rectangle is. (float)
height = float(input("Height: "))
#calculates area
sum = (width * height)
#prints the calculated answer in 2 decimal places
print("\nArea of Rectangle:", round(sum, 2))
#makes sure the user clicks enter before the "console" closes. this allows them to see the answer instead of the console closing instantly
input()