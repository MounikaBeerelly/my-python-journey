"""
Scenario: Write a program that can add two numbers and present the result

Algorithm:
----------
1. design the process 01 for collecting 2 values from the end user and assigning into two variables
2. Design the process 02 for adding the 2 values and store the result in another variable
3. Design the rocess 03 for displaying the result to the end user.

Approach:
---------
1. Modular programming approach

Methodology followed
--------------------
1. Functions accepting any parameters and returning a value

Pseudo syntax:
-------------
def functionName(inParam01,inParam02,...):
    Body of the function
    return returnValue
"""

#!python3

import os
os.system("cls")

def addValues(inOperand01,inOperand02):
    
    result = inOperand01 + inOperand02
    
    print("\nThe sum of", inOperand01, "and", inOperand02, "is: ", end="")

    return result

print("\nCalling the \"addValues()\" function",end="\n")

operand01 = int(input("\nPlease enter the first value: "))
operand02 = int(input("\nPlease enter the second value: "))

resultValue = addValues(operand01,operand02)

print(resultValue, end="\n")