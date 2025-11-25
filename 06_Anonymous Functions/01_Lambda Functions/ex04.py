#!python3

import os
os.system("cls")

# Using Normal function
def setValue() :
    """Assigning a given value using normal function"""
    inValue = int(input("\nPlease enter any Numerical value: "))
    return inValue

def getValue() :
    """Returning the requested number using normal function"""
    retValue = setValue()
    return retValue

print("\nThe given value by the end user is: ", getValue(), end="\n")

"""
Output:
-------
Please enter any Numerical value: 12

The given value by the end user is:  12
"""

# Using Lambda function
setValueLF = lambda : int(input("\nPlease enter any Numerical value: "))

getValueLF = lambda : print("\nThe given value by the end user is: ", setValueLF(), end="\n")

getValueLF()

"""
Output:
=======
Please enter any Numerical value: 76

The given value by the end user is:  76
"""