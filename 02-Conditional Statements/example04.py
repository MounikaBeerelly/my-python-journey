"""
Scenario:
---------
Write a program for even number and odd number test, as a single liner logic including the output statements.
"""

#!python3

import os
os.system("cls")

inValue = int(input("\nPlease enter any numerical value: "))
print("\nThe given number is: ",inValue,end="\n")

if ((inValue % 2)==0): print("\nThe given value",inValue,"is an Even number",end="\n")
else: print("\nThe given value",inValue,"is an odd number",end="\n")


"""
Scenario:
---------
Write a program for even number and odd number test, as a single liner logic, designing any branching logic as an expression including the output statements.
"""

#!python3

import os
os.system("cls")

inValue = int(input("\nPlease enter any numerical value: "))
print("\nThe given number is: ",inValue,end="\n")

finalResult = "The given value is and Even number"if((inValue % 2)==0) else"The given number isan odd number"
print(finalResult,end="\n")
