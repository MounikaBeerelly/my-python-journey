#!python3

import os
os.system("cls")

# Using Lambda function

findSquare = lambda param01 : param01 * param01
findCube = lambda param01 : findSquare(param01) * param01

print("\nPlease enter your choice from the menu", end="\n")
print("\n1. Square the value")
print("\n2. Cube the value")
print("\n0. Exit")

inChoice = input("\nPlease enter your choice of operation: ")
inValue = int(input("\nPlease enter the value : "))

if inChoice == '1' :
    print("\nThe square of the number ", inValue, "is:", findSquare(inValue), end="\n")
elif inChoice == '2' :
        print("\nThe cube of the number ", inValue, "is:", findCube(inValue), end="\n")
else :
    print("\nYou requested to exit the process", end="\n")
    

"""
Output:
-------
Please enter your choice from the menu

1. Square the value

2. Cube the value

0. Exit

Please enter your choice of operation: 2

Please enter the value : 5

The cube of the number  5 is: 125
"""