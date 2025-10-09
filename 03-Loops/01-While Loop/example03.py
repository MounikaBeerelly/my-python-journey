 
"""
Scenario:
---------
Write a program to print sequence of natural numbers, Given the start value and end range specified by the end user.
Sample output: 1 2 3 4 5

Validations to check:
---------------------
1. The process should initiate only when the first value is provided
2. when the first value is found then only process to take the second value
3. Manage proper messaging and termination states when the validations are violated
"""

#!python3

import sys
import os
os.system("cls")

startRange =  endRange = 0

startRange = input("\nPlease enter the starting range value to print the series:")

if startRange:
    startRange = int(startRange)
    endRange = input("\nPlease enter the ending range value to terminate the series:")
    if endRange:
        endRange = int(endRange)
    else:
        sys.exit("\nSorry! cannot continue, the end range not be defined...")
else:
    sys.exit("\nSorry! cannot continue, The start range not be defined..")

print("\nThe sequence of numbers expected to generate are from %d To %d,"%(startRange,endRange), end="\n")

print("\nInitializing the loop for execution.. Please wait..",end="\n")
print("\nPrinting the sequence of numbers from %d To %d,"%(startRange,endRange),"are:",end="\n")

while(startRange <= endRange):
    print("%d"%(startRange),end=" ") 
    startRange = startRange + 1

#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")

