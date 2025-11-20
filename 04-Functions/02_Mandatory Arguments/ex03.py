#!python3

import time

import os
os.system("cls")

def printGreeting(inOperand01, inOperand02) :
    # function to print Greeting for parameters passed as mandatory parameters
    print("\nThe given value for Greeting is: ", inOperand01, end="\n")
    print("\nThe given value for quantifying is: ", inOperand02, end="\n")
    
    result = inOperand01 * inOperand02
    print("\nThe final result is: ", inOperand01, " and", inOperand02, " is: ", result, end="\n")
    return

print("\nThis is the main module", end="\n")
print("--------------------------", end="\n")
operand01 = input("\nPlease enter the first value : ")
operand02 = input("\nPlease enter the second value : ")

print("\nIllustration of mandatory OR required positional notation", end="\n")
print("-----------------------------------------------------------", end="\n")

print("\nCalling the function exactly by the given position of the formal parameters...", end="\n")
printGreeting(operand01, operand02)

print("\nCalling the function by the swapping the position of the actual parameters...", end="\n")
printGreeting(int(operand02), int(operand01))

print("\nCalling the function by the swapping the position of the actual parameters...", end="\n")
printGreeting(operand02, int(operand01))

"""
Output
=======
This is the main module
--------------------------

Please enter the first value : 23

Please enter the second value : 10

Illustration of mandatory OR required positional notation
-----------------------------------------------------------

Calling the function exactly by the given position of the formal parameters...

The first argument "inOperand1" is:  23

The second argument "inOperand2" is:  10

The subtraction of 23  and 10  is:  13

Calling the function by the swapping the position of the actual parameters...

The first argument "inOperand1" is:  10

The second argument "inOperand2" is:  23

The subtraction of 10  and 23  is:  -13
"""