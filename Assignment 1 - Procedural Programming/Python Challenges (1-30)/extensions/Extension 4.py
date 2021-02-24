#defining total as 0
total = 0
#define i as 0
i = 0
#while loop that gets 3 user inputs then adds them
while i < 3:
    sum_of_numbers = int(input("Enter a number: "))
    total += sum_of_numbers
    i += 1
#outputs the sum from the while loop
print("\nSum:", total)
#allows users to see output
input()