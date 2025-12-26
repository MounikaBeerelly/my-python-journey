#!python3

import os
os.system("cls")

def myCache(inFunction) :
    cacheMemory = {}
    def execFactorial(inValue) :
        if inValue in cacheMemory :
            return cacheMemory[inValue]
        else: 
            finalResult = inFunction(inValue)
            cacheMemory[inValue] = finalResult
            return finalResult
    return execFactorial

def calculateFactorial(inValue) :
    if inValue == 0 :
        return 1
    else :
        return inValue * myCache(calculateFactorial)(inValue - 1)

if __name__ == "__main__" :
    print("\nProgram to calculate factorial with custom cache management", end="\n")
    
    actualValue = int(input("\nPlease enter the number for cakculating the factorial: "))
    print("\nThe factorial of %d is: %d"%(actualValue, calculateFactorial(actualValue)), end="\n")
    
"""
Output:
-------
Program to calculate factorial with custom cache management

Please enter the number for cakculating the factorial: 8

The factorial of 8 is: 40320
"""