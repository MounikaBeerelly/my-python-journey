#!python3

import os
os.system("cls")

def outerFunction() :
    # outer function scope "Local to itself" and "Encloseding scope to inner function"
    outerMessage = "Hello, I am responding from Enclosing scope"
    def innerFunction() :
        # Inner function operating as nested function having only local scope to itself
        print("\nData from enclsoing variable printed from inner function is : ", outerMessage, end="\n")
        return 
    
    print("\nThe inner function scope is at : ", innerFunction, end="\n")
    print("\nCalling the inner function is...", end="\n")
    return innerFunction

if __name__ == "__main__" :
    outerFunctionAddress = outerFunction
    returnAddressOfInnerFunction = outerFunctionAddress()
    print("\nThe return value of the outer function call : ", returnAddressOfInnerFunction, end="\n")
    

"""
Output:
-------
The inner function scope is at :  <function outerFunction.<locals>.innerFunction at 0x0000026D6B83D700>

Calling the inner function is...

The return value of the outer function call :  <function outerFunction.<locals>.innerFunction at 0x0000026D6B83D700>
"""