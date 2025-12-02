#!python3

import os
os.system("cls")

from functools import partial

def addValues(inParam01, inParam02, inParam03) :
    # function to add 3 numbers supplied through parameters
    return inParam01 + inParam02 + inParam03  

if __name__ == "__main__" :
    print("\nCreating a partial function by fixing the first parameter to any given constant value...", end="\n")
    inParam01 = int(input("\nPlease give the first parameter: "))
    
    partialAdd = partial(addValues, inParam01) # here the partial function fixes the value to the first parameter as given value
    
    finalResult = partialAdd(10, 15) #At run-time this partialAdd function operates as addValues(inParam01, 10, 15)
    
    print("\nThe final result of the expression is: ", finalResult, end="\n")
    
"""
Output:
-------
Creating a partial function by fixing the first parameter to any given constant value...

Please give the first parameter: 12

The final result of the expression is:  37
"""