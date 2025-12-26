"""
Scenario:
---------
Write a program to find the factorial of a given number at run time, in the following format.
Sample output
--------------
1 = 1
1*2 = 2
1*2*3 = 6
1*2*3*4 = 24
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

factIndex = factValue = 1

while(factIndex <= factNumber):
    factValue *= factIndex
    if factIndex == 1:
        print("1 = 1")
    else:
        genIndex = 2
        print("1",end=" ")
        while(genIndex <= factIndex):
            print("* %d"%(genIndex),end=" ")
            genIndex += 1
        print("= %d"%(factValue))
    factIndex += 1
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")

