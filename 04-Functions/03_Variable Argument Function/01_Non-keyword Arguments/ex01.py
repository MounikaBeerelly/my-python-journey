#!python3

import time

import os
os.system("cls")

def addValues(*args) :
    # function to add values passed as parameters dynamically at run time
    calculateSum = 0
    print("The value read is: ", end="")
    for myValueIndex in args :
        print(myValueIndex, end=", ")
        calculateSum = calculateSum + myValueIndex
        
    print("\n\nThe total sum of all the supplied argument values is: ", calculateSum, end = "\n")
    return 

print("\nThis is the main module..", end="\n")
print("---------------------------", end="\n")

executeChoice = int(input("\nHow many argumentns you have to operate: "))

if executeChoice == 1 :
    operand01 = int(input("\nPlease enter the only argument you have: "))
    addValues(operand01)
elif executeChoice == 2 :
    operand01 = int(input("\nPlease enter the first value: "))
    operand02 = int(input("\nPlease enter the second value: "))
    addValues(operand01, operand02)
elif executeChoice == 3 :
    operand01 = int(input("\nPlease enter the first value: "))
    operand02 = int(input("\nPlease enter the second value: "))
    operand03 = int(input("\nPlease enter the third value: "))
    addValues(operand01, operand02, operand03)
elif executeChoice == 4 :
    operand01 = int(input("\nPlease enter the first value: "))
    operand02 = int(input("\nPlease enter the second value: "))
    operand03 = int(input("\nPlease enter the third value: "))
    operand04 = int(input("\nPlease enter the fourth value: "))
    addValues(operand01, operand02, operand03, operand04)
else:
    print("\nSorry Un-known abnormally is encountered, contact the developer..", end="\n")
    
    
"""
Output:
-------

This is the main module..
---------------------------

How many argumentns you have to operate: 3

Please enter the first value: 12

Please enter the second value: 6

Please enter the third value: 23
The value read is: 12, 6, 23,

The total sum of all the supplied argument values is:  41
"""