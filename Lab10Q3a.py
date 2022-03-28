# program to output a module name based on module code input

# prompt user to enter module code
code = input("Enter a module code: ")

# use dict for a simple lookup as python does not have a switch-case construct
switcher={
    'CSC1001':'Introduction to Computing',
    'CSC1008':'Data Structures and Algorithms',
    'CSC1009':'Object-Oriented Programming',
    'CSC1010':'Computer Networks'
}

# print out module name based on input code
print(switcher[code])
