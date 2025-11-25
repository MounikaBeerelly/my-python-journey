#!python3

import os
os.system("cls")

# Using normal function
def getValue(inParam01) :
    """Returning a given number using normal function"""
    return inParam01

inValue01 = int(input("\nPlease enter the value 01: "))

print("\nThe given value returned by normal function is : ", getValue(inValue01), end="\n")

"""
Output:
------
Please enter the value 01: 45

The given value returned by normal function is :  45
"""

# using lambda function

getValueLF = lambda inParam02: inParam02

inValue02 = int(input("\nPlease enter the value 02: "))

print("\nThe given value returned by lambda function is : ", getValueLF(inValue02), end="\n")


"""
Output:
-------
Please enter the value 02: 76

The given value returned by lambda function is :  76
"""