#!python3

import os
os.system("cls")

import mathsModule as myMath # Here we are importing the module that is created by us and saved to the same directory where this current program is available

print("\nWe are in the Main block of the Python program", end="\n")
print("------------------------------------------------", end="\n")

operand01 = int(input("\nPlease enter the first value : "))
operand02 = int(input("\nPlease enter the second value : "))

resultValue = myMath.addValues(operand01, operand02) # here we are providing reference of a MathsModule to addValues() function

print(resultValue, end="\n")

print("\nReturned from the addValues() function locally declared, will continue in the main block", end="\n")
print("\nOperating in the main block, after functional call is completed", end="\n")


"""
Output:
-------
We are in the Main block of the Python program
------------------------------------------------

Please enter the first value : 11

Please enter the second value : 5

The sum of 11 And 5 is : 16

Returned from the addValues() function locally declared, will continue in the main block

Operating in the main block, after functional call is completed
"""