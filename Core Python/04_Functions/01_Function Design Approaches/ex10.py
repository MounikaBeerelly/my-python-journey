#!python3

"""
Scenario:
---------
1. Write a program that can execute the required ,athematical operations for the operator type given as input with the corresponding required operands.
2. Use all the commonsense based validations upon the actual code
"""

import os
os.system("cls")

def addValues(inOperand01,inOperand02):
    """Function to add two values passed as input parameters"""
    outResult = inOperand01 + inOperand02
    return outResult

def subtractValues(inOperand01,inOperand02):
    """Function to subtract two values passed as input parameters"""
    outResult = inOperand01 - inOperand02
    return outResult

def multiplyValues(inOperand01,inOperand02):
    """Function to multiply two values passed as input parameters"""
    outResult = inOperand01 * inOperand02
    return outResult    

def divideValues(inOperand01,inOperand02,inDivisionType):
    """Function to divide two values passed as input parameters"""
    if(inDivisionType == '/'):
        outResult = inOperand01 / inOperand02
    else:
        outResult = inOperand01 % inOperand02
    return outResult

print("\nApplication to implement the mathematical operations")
print("-------------------------------------------------------",end="\n")

inOperand01 = float(input("\nPlease enter the first number:"))
inOperand02 = float(input("\nPlease enter the second number:"))
inOperator = input("\nPlease enter the operator to execute the mathematical expression(+,-,*,/,%):")

if(inOperator == '+' or inOperator == '-' or inOperator == '*' or inOperator == '/'):
    if inOperator == '+':
        retResult = addValues(inOperand01,inOperand02)
        print("\nThe sum of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
    elif inOperator == '-':
        retResult = subtractValues(inOperand01,inOperand02)
        print("\nThe difference of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
    elif inOperator == '*':
        retResult = multiplyValues(inOperand01,inOperand02)
        print("\nThe product of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
    else:
        if inOperand02 != 0:
            divisionType = input("\nPlease enter the resukt of the division to calculate (Quotient: Q OR Reminder:R):")
            if(divisionType == 'Q' or divisionType == 'q') or (divisionType == 'R' or divisionType == 'r'):
                if(divisionType == 'Q' or divisionType == 'q'):
                    inDivisionType = '/'
                    retResult = divideValues(inOperand01,inOperand02,inDivisionType)
                    print("\nThe quotient of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
                else:
                    inDivisionType = '%'
                    retResult = divideValues(inOperand01,inOperand02,inDivisionType)
                    print("\nThe Reminder of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
            else:
                print("\nSorry! The type of the definition selected for operation is invalid, try once again...",end="\n")
        else:
            print("\nSorry! Division cannot be executed when the determinator is zero",end="\n")