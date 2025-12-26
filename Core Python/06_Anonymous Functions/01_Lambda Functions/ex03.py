#!python3

import os
os.system("cls")

inValue = int(input("\nPlease enter the value: "))

print("\nImplementing the concept of Anonymous function", end="\n")

getValueLF = lambda : print("\nThe given value by the end user is : ", inValue, end="\n")

getValueLF()

"""
Output:
-------
Please enter the value: 51

Implementing the concept of Anonymous function

The given value by the end user is :  51
"""