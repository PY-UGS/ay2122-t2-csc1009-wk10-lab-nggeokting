# program to take in 2 numbers and output their average

# take in keyboard input for 2 numbers (x and y)
x = input("Enter first number: ")
y = input("Enter second number: ")

# calculate average of the 2 numbers
average = (float(x) + float(y)) / 2

# print average of the 2 numbers
print("The average of {x} and {y} is {average}".format(x=x, y=y, average=average))
