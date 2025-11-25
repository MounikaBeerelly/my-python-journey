#!python3

import os
os.system("cls")

# ----------- Using Normal function -----------------
def addNumbers(param01, param02) :
    return param01 + param02

def subtractNumbers(param01, param02) :
    return param01 - param02

def multiplyNumbers(param01, param02) :
    return param01 * param02

def divideNumbers(param01, param02, inDivisionType) :
    if inDivisionType == '/' :
        return param01 / param02
    else :
        return param01 % param02

inOperand01 = float(input("\nPlease enter the first number:"))
inOperand02 = float(input("\nPlease enter the second number:"))
inOperator = input("\nPlease enter the operator to execute the mathematical expression(+,-,*,/,%):")

if(inOperator == '+' or inOperator == '-' or inOperator == '*' or inOperator == '/'):
    if inOperator == '+':
        retResult = addNumbers(inOperand01,inOperand02)
        print("\nThe sum of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
    elif inOperator == '-':
        retResult = subtractNumbers(inOperand01,inOperand02)
        print("\nThe difference of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
    elif inOperator == '*':
        retResult = multiplyNumbers(inOperand01,inOperand02)
        print("\nThe product of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
    else:
        if inOperand02 != 0:
            divisionType = input("\nPlease enter the result of the division to calculate (Quotient: Q OR Reminder:R):")
            if(divisionType == 'Q' or divisionType == 'q') or (divisionType == 'R' or divisionType == 'r'):
                if(divisionType == 'Q' or divisionType == 'q'):
                    inDivisionType = '/'
                    retResult = divideNumbers(inOperand01,inOperand02,inDivisionType)
                    print("\nThe quotient of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
                else:
                    inDivisionType = '%'
                    retResult = divideNumbers(inOperand01,inOperand02,inDivisionType)
                    print("\nThe Reminder of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,retResult),end="\n")
            else:
                print("\nSorry! The type of the definition selected for operation is invalid, try once again...",end="\n")
        else:
            print("\nSorry! Division cannot be executed when the determinator is zero",end="\n")
"""
Output:
=======
Please enter the first number:12

Please enter the second number:12

Please enter the operator to execute the mathematical expression(+,-,*,/,%):/

Please enter the resukt of the division to calculate (Quotient: Q OR Reminder:R):q

The quotient of 12.00 and 12.00 is: 1.00
"""

# -----------------Using Lambda function-----------------
addNumbersLF = lambda param01, param02 : param01 + param02
subtractNumbersLF = lambda param01, param02 : param01 - param02
multiplyNumbersLF = lambda param01, param02 : param01 * param02
divideNumbersLF = lambda param01, param02 : param01 / param02
reminderValuesLF = lambda param01, param02 : param01 % param02

print("\nPerform the Mathematical Operations", end="\n")
print("------------------------------------------", end="\n")

print("\nPlease enter the choice from Menu", end="\n")
print("\n1. Addition")
print("\n2. Subtraction")
print("\n3. Multiplication")
print("\n4. Division : Quotient")
print("\n5. Division : Reminder")
print("\n0. Exit")

inChoice = input("\nPlease enter your choice: ")
inOperand01 = float(input("\nPlease enter the first number:"))
inOperand02 = float(input("\nPlease enter the second number:"))

if inChoice == '1':
    print("\nThe sum of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,addNumbersLF(inOperand01, inOperand02)),end="\n")
elif inChoice == '2':
    print("\nThe difference of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,subtractNumbersLF(inOperand01, inOperand02)),end="\n")
elif inChoice == '3':
    print("\nThe product of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,multiplyNumbersLF(inOperand01, inOperand02)),end="\n")
elif inChoice == '4':
    print("\nThe Quotient of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,divideNumbersLF(inOperand01, inOperand02)),end="\n")
elif inChoice == '5':
    print("\nThe Remainder of %0.2f and %0.2f is: %0.2f"%(inOperand01,inOperand02,reminderValuesLF(inOperand01, inOperand02)),end="\n")
else:
    print("\nSorry! Improper operator identified, cannot proceed with Mathematical evaluation...",end="\n")
"""
Output:
=======
Perform the Mathematical Operations
------------------------------------------

Please enter the choice from Menu

1. Addition

2. Subtraction

3. Multiplication

4. Division : Quotient

5. Division : Reminder

0. Exit

Please enter your choice: 3

Please enter the first number:12

Please enter the second number:12

The product of 12.00 and 12.00 is: 144.00
"""
