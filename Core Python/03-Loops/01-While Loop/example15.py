"""
Scenario:
---------
Write a program to accept any number from the end user and find all the positive factors of the given number.

Points to notice:
=================
- Do not use any existing python modules OR libraries OR built-in functions

Domain Knowledge:
-----------------
1. A factor of a given number is an "integer" that can be multiplied together to produce that number
2. Formal definition
    - If we have a number "n", its identified factors are the integers "a" and "b" then a*b = n
    
Algorithm:
---------
1. Input the number: Prompt the end user to input the number
2. Set and initialize the required variables for
    1. Managing the loop index
    2. The factor number to be found with 1
3. Design a "Loop"
    1. Check the condition such that "loop index" <= "input number"
    2. Check for factor
        1. "Input number" % "loop index" == 0 then the "loop index" is a factor of "input number"
        2. If the above condition is true, then print the factor as "loop index"
    3. Update the loop status by incrementing with 1
"""

#!python3

import os
import math
os.system("cls")

loopIndex = factorNumber = 1

factorNumber = int(input("\nPlease enter any number to find factors:"))

print("\nDisplaying all the factors of %d:"%(factorNumber), end="\n")

while(loopIndex <= factorNumber):
    if(factorNumber % loopIndex == 0):
        print("%d"%(loopIndex),end=",")
    loopIndex += 1

# Without traversing the entire range of the given number
while(loopIndex <= (factorNumber//2)):
    if(factorNumber % loopIndex == 0):
        print("%d"%(loopIndex),end=",")
    loopIndex += 1

print("%d"%(factorNumber),end=",")

# Using relevant packages in python
while(loopIndex <= math.sqrt(factorNumber)):
    if(factorNumber % loopIndex == 0):
        print("%d"%(loopIndex),end=",")
        
        if loopIndex != factorNumber//loopIndex:
            print("%d,"%(factorNumber//loopIndex),end="")
    loopIndex += 1
    
print()