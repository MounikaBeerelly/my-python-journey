"""
Scenario:
---------
Write a program to find the factorial of a given number at run time, in the following format.
Sample output
--------------
5 = 5
5 * 4 = 20
5 * 4 * 3 = 60
5 * 4 * 3 * 2 = 120
5 * 4 * 3 * 2 * 1 = 120
"""

#!python3

import os
import sys
os.system("cls")

print("\nIllustration of \"WHILE\" loop in python")
print("------------------OoO----------------",end="\n")

factNumber = int(input("\nPlease enter the value for finding the factorial:"))

if factNumber < 0:
    sys.exit("\nCannot take factorial for negative numbers..")

if factNumber == 0:
    sys.exit("\nSorry! cannot calculate the factorial for zero..")
    
if factNumber == 1:
    sys.exit("\nThe factorial of 1 is: 1")

if factNumber == 2:
    sys.exit("\nThe factorial of 2 is: 2")

factIndex = factNumber
factValue = 1
finalOutput = ""

while(factIndex > 0):
    factValue *= factIndex
    if (factIndex == factNumber):
        finalOutput = f"{factIndex}"
    else:
        finalOutput += f" * {factIndex}"
    
    print(f"{finalOutput} = {factValue}")
    factIndex -= 1          
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")

