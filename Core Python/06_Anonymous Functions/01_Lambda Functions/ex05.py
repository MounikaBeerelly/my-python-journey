#!python3

import os
os.system("cls")

# Using Normal function
def addNumbers(param01, param02) :
    return param01 + param02

value01 = int(input("\nPlease enter the value 01: "))
value02 = int(input("\nPlease enter the value 02: "))

finalResult = addNumbers(value01, value02)

print("\nThe sum of", value01, "and", value02, "is: ", finalResult, end="\n")

"""
Output:
=======
Please enter the value 01: 10

Please enter the value 02: 30

The sum of 10 and 30 is:  40
"""

# Using Lambda function
addNumbersLF = lambda inParam01, inParam02 : inParam01 + inParam02

inValue01 = int(input("\nPlease enter the value 01: "))
inValue02 = int(input("\nPlease enter the value 02: "))

print("\nThe sum of", inValue01, "and", inValue02, "is: ", addNumbersLF(inValue01, inValue02), end="\n")

"""
Output:
=======
Please enter the value 01: 14

Please enter the value 02: 52

The sum of 14 and 52 is:  66
"""