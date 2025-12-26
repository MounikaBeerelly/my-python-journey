#!python3

import os
os.system("cls")

import mathsModule as myMath # Here we are importing the module that is created by us and saved to the same directory where this current program is available

def minusValues(param01, param02) :
    # function to minus two values, accepting parameters and returning value
    
    result = param01 - param02
    
    print(f"\nThe Difference of {param01} And {param02} is : ", end = "")
    return result

print("\nWe are in the Main block of the Python program", end="\n")
print("------------------------------------------------", end="\n")

operand01 = int(input("\nPlease enter the first value : "))
operand02 = int(input("\nPlease enter the second value : "))

sumValue = myMath.addValues(operand01, operand02) # here we are providing reference of a MathsModule to addValues() function

print(sumValue, end="\n")

subtractValue = minusValues(operand01, operand02)
print(subtractValue, end="\n")

"""
Output:
-------

We are in the Main block of the Python program
------------------------------------------------

Please enter the first value : 67

Please enter the second value : 43

The sum of 67 And 43 is : 110

The Difference of 67 And 43 is : 24

"""