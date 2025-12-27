#!python3

import time

import os
os.system("cls")

def findMaximum(*args) :
   #function to find the maximum of given numbers
   print("\nThe given numbers from the end user is:", args, end="\n")
   return max(args)

print("\nThe main application begins here...", end="\n")

print("\nThe given numbers are \"10\", \"15\", maximum of the given values is: ", findMaximum(10,15), end="\n")
print("\nThe given numbers are \"10\", \"63\", \"48\" maximum of the given values is: ", findMaximum(10,63,48), end="\n")
print("\nThe given numbers are \"36\", \"12\", \"76\", \"3\", maximum of the given values is: ", findMaximum(36,12,76,3), end="\n") 
 
    
"""
Output:
-------
The main application begins here...

The given numbers from the end user is: (10, 15)

The given numbers are "10", "15", maximum of the given values is:  15

The given numbers from the end user is: (10, 63, 48)

The given numbers are "10", "63", "48" maximum of the given values is:  63

The given numbers from the end user is: (36, 12, 76, 3)

The given numbers are "36", "12", "76", "3", maximum of the given values is:  76
"""
