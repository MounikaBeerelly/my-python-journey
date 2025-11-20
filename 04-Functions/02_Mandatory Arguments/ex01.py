#!python3

import time

import os
os.system("cls")

def addValues(inOperand01, inOperand02) :
    # function to add two values passed as mandatory parameters
    print("\nThe first argument \"inOperand1\" is: ", inOperand01, end="\n")
    print("\nThe second argument \"inOperand2\" is: ", inOperand02, end="\n")
    result = inOperand01 + inOperand02
    print("\nThe sum of", inOperand01, " and", inOperand02, " is: ", result, end="\n")
    return

print("\nThis is the main module", end="\n")
print("--------------------------", end="\n")
operand01 = int(input("\nPlease enter the first value : "))
operand02 = int(input("\nPlease enter the second value : "))

print("\nIllustration of mandatory OR required positional notation", end="\n")
print("-----------------------------------------------------------", end="\n")

print("\nCalling the function exactly by the given position of the formal parameters...", end="\n")
addValues(operand01, operand02)

print("\nCalling the function by the swapping the position of the actual parameters...", end="\n")
addValues(operand02, operand01)

"""
Output
=======

This is the main module
--------------------------

Please enter the first value : 23

Please enter the second value : 65

Illustration of mandatory OR required positional notation
---------------------------------------------------------

Calling the function exactly by the given position of the formal parameters...

The first argument "inOperand1" is:  23

The second argument "inOperand2" is:  65

The sum of 23  and 65  is:  88

Calling the function by the swapping the position of the actual parameters...

The first argument "inOperand1" is:  65

The second argument "inOperand2" is:  23

The sum of 65  and 23  is:  88

"""

"""
Note:
-----
1. Calling the function by supplying the arguments by position, which is called as Positional Notation
2. When we call any function by just passing the values as actual parameters, the given actual parameter values in actual environment will be copied into the "Formal Parameters" of the function definition exactly as per the declared position of the "Formal Parameters", this kind of parameter substitution by exact position is called as "Positional Notation".
    - Basic Illustration :
    -----------------------
    def addValues(inOperand01, inOperand02) :
                       ^             ^
                       |             |  Positional notation
            addValues(operand01, operand02)
            
- When positional notation is used in function call, all the supplied "Actual Parameters" should follow the exact order of declaration defined in the "Functions Definition".
    - Any time the order of the "Actual Parameters" in the "Fucntion call" is mis-matching to the declared order of the "types" of the "Formal Parameters" either
        - Logically the operational state of the function will be wrong OR
        - The function at run-time can generate an error due to "Type Mis-Match" 
"""