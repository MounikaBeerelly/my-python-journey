#!python3

import os
os.system("cls")

# without Decorators
def executeDivision(inNumerator, inDenominator) :
    if inDenominator == 0 :
        return "Fatal Error! Cannot divide by zero.."
    else :
        return inNumerator / inDenominator

def validateDivision(inNumerator, inDenominator) :
    if inDenominator == 0 :
        print("\nSorry! validation failed : Division by zero..", end="\n")
        return "Error"
    else :
        return executeDivision(inNumerator, inDenominator)

if __name__ == "__main__" :
    print("\n------- Without Decorators ---------------", end="\n")
    inNumerator = int(input("\nPlease enter the Numerator value : "))
    inDenominator = int(input("\nPlease enter the Denominator value : "))
    
    print(f"\nThe final Quotient is : {validateDivision(inNumerator, inDenominator)}", end="\n")
    
# with Decorators

def validateDivision(inFunctionName) :
    def wrapperFunction(inNumerator, inDenominator) :
        if inDenominator == 0 :
            print("\nSorry! validation failed : Division by zero..", end="\n")
            return "Error"
        return inFunctionName(inNumerator, inDenominator)
    return wrapperFunction

@validateDivision
def executeDivision(inNumerator, inDenominator) :
    if inDenominator == 0 :
        return "Fatal Error! Cannot divide by zero.."
    else :
        return inNumerator / inDenominator

if __name__ == "__main__" :
    print("\n------- With Decorators ---------------", end="\n")
    inNumerator = int(input("\nPlease enter the Numerator value : "))
    inDenominator = int(input("\nPlease enter the Denominator value : "))
    
    print(f"\nThe final Quotient is : {executeDivision(inNumerator, inDenominator)}", end="\n")
    
"""
Output:
-------
------- Without Decorators ---------------

Please enter the Numerator value : 46

Please enter the Denominator value : 0

Sorry! validation failed : Division by zero..

The final Quotient is : Error

------- With Decorators ---------------

Please enter the Numerator value : 45

Please enter the Denominator value : 5

The final Quotient is : 9.0
"""