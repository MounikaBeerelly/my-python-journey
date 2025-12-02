#!python3

import os
os.system("cls")

from functools import partial

def multiplyNumbers(inParam01, inParam02, inParam03) :
    return inParam01 * inParam02 * inParam03

if __name__ == "__main__" :
    print("\nCreating a partial function by fixing some of the arguments", end="\n")
    
    dblmultiplier = int(input("\nPlease give value for the double multiplier: "))
    doubleMultiplier = partial(multiplyNumbers, dblmultiplier) # here we are fixing the value to the inParam01 assigned with the given value of dblMultiplier
    
    trplmultiplier = int(input("\nPlease give value for the triple multiplier: "))
    tripleMultiplier = partial(multiplyNumbers, trplmultiplier) # here we are fixing the value to the inParam01 assigned with the given value of trplMultiplier
    
    print("\nImplementing the multiplication of any given two numbers by the value supplied for \"dblMultiplier\" variable", end="\n")
    inParam02 = int(input("\nPlease give value for second parameter: "))
    inParam03 = int(input("\nPlease give value for third parameter: "))
    print("\nThe final value of the \"doubleMultiplier\" function when called is: ", doubleMultiplier(inParam02, inParam03), end="\n")

    print("\nImplementing the multiplication of any given two numbers by the value supplied for \"trplMultiplier\" variable", end="\n")
    inParam02 = int(input("\nPlease give value for second parameter: "))
    inParam03 = int(input("\nPlease give value for third parameter: "))
    print("\nThe final value of the \"tripleMultiplier\" function when called is: ", tripleMultiplier(inParam02, inParam03), end="\n")

"""
Output:
-------

Creating a partial function by fixing some of the arguments

Please give value for the double multiplier: 2

Please give value for the triple multiplier: 3

Implementing the multiplication of any given two numbers by the value supplied for "dblMultiplier" variable

Please give value for second parameter: 6

Please give value for third parameter: 5

The final value of the "doubleMultiplier" function when called is:  60

Implementing the multiplication of any given two numbers by the value supplied for "trplMultiplier" variable

Please give value for second parameter: 4

Please give value for third parameter: 5

The final value of the "tripleMultiplier" function when called is:  60
"""