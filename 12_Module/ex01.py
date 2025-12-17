#!python3

import os
os.system("cls")

import mathsModule # Here we are importing the module that is created by us and saved to the same directory where this current program is available

print("\nWe are in the Main block of the Python program", end="\n")
print("------------------------------------------------", end="\n")

operand01 = int(input("\nPlease enter the first value : "))
operand02 = int(input("\nPlease enter the second value : "))

resultValue = mathsModule.addValues(operand01, operand02) # here we are providing reference of a MathsModule to addValues() function

print(resultValue, end="\n")

print("\nReturned from the addValues() function locally declared, will continue in the main block", end="\n")
print("\nOperating in the main block, after functional call is completed", end="\n")


"""
Output:
-------

We are in the Main block of the Python program
------------------------------------------------

Please enter the first value : 12

Please enter the second value : 45

The sum of 12 And 45 is : 57

Returned from the addValues() function locally declared, will continue in the main block

Operating in the main block, after functional call is completed
"""