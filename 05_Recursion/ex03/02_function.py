"""
Scenario:
---------
Write a program to find the factorial of a given number at runtime

1. The above concept can be implemented using the loop based approach as the process is iterative begining for an "Initial state" and multiplying sequence of numbers in the process 
"""

import os
import sys
os.system("cls")

def calculateFactorial(inParam) :
    """function to calculate the factorial of a given number"""
    factValue = 1
    for factIndex in range(2, factorialValue + 1) :
        factValue = factValue * factIndex
    return factValue

factValue = 1

factorialValue = int(input("\nPlease enter the number to calculate factorial : "))

print("\nCalculating the factorial of :", factorialValue, end="\n")

if factorialValue == 0 :
    sys.exit("\nZero factorial is not calculate, hence terminating the application...")
if factorialValue == 1 :
    sys.exit("\nThe factorial for 1 is: 1")
if factorialValue == 2:
    sys.exit("\nThe factorial for 2 is: 2")
    
factValue = calculateFactorial(factorialValue)

print("\nThe factorial of ", factorialValue, "is: ", factValue, end="\n")
    
"""
Output:
-------
Please enter the number to calculate factorial : 8

Calculating the factorial of : 8

The factorial of  8 is:  40320
"""