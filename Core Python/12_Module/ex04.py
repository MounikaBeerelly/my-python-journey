#!python3

import os
os.system("cls")

from mathsModule import subtractValues # Here we are importing the module that is created by us and saved to the same directory where this current program is available

print("\nWe are in the Main block of the Python program", end="\n")
print("------------------------------------------------", end="\n")

operand01 = int(input("\nPlease enter the first value : "))
operand02 = int(input("\nPlease enter the second value : "))

differenceValue = subtractValues(operand01, operand02)

print(differenceValue, end="\n")

"""
Output:
-------
We are in the Main block of the Python program
------------------------------------------------

Please enter the first value : 45

Please enter the second value : 11

The Difference of 45 And 11 is : 34
"""