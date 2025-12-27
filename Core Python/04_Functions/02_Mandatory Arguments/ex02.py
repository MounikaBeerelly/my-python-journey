#!python3

import time

import os
os.system("cls")

def subtractValues(inOperand01, inOperand02) :
    # function to subtract two values passed as mandatory parameters
    print("\nThe first argument \"inOperand1\" is: ", inOperand01, end="\n")
    print("\nThe second argument \"inOperand2\" is: ", inOperand02, end="\n")
    result = inOperand01 - inOperand02
    print("\nThe difference of", inOperand01, " and", inOperand02, " is: ", result, end="\n")
    return

print("\nThis is the main module", end="\n")
print("--------------------------", end="\n")
operand01 = int(input("\nPlease enter the first value : "))
operand02 = int(input("\nPlease enter the second value : "))

print("\nIllustration of mandatory OR required positional notation", end="\n")
print("-----------------------------------------------------------", end="\n")

print("\nCalling the function exactly by the given position of the formal parameters...", end="\n")
subtractValues(operand01, operand02)

print("\nCalling the function by the swapping the position of the actual parameters...", end="\n")
subtractValues(operand02, operand01)

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

The difference of 23  and 10  is:  13

Calling the function by the swapping the position of the actual parameters...

The first argument "inOperand1" is:  10

The second argument "inOperand2" is:  23

The difference of 10  and 23  is:  -13
"""