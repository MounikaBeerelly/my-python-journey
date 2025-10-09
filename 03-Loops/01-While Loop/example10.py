"""
Scenario:
---------
Write a program to find the factorial of a given number at runtime
"""

#!python3

import sys
import os
os.system("cls")

factValue = factNumber = factIndex = 1

factNumber = int(input("\nPlease enter the value for finding the factorial:"))

factIndex = factNumber

if factNumber < 0:
    sys.exit("\nCannot take factorial for negative numbers..")

if factNumber == 0:
    sys.exit("\nSorry! cannot calculate the factorial for zero..")
    
if factNumber == 1:
    sys.exit("\nThe factorial of 1 is: 1")

if factNumber == 2:
    sys.exit("\nThe factorial of 2 is: 2")

while(factIndex >= 1):
    factValue = factValue * factIndex
    factIndex -= 1

print("\n\nthe factorial of %d is = %d"%(factNumber,factValue), end="\n")
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")



