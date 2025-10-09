"""
Scenario: Write a program to check a variable is carrying any value OR not, given at run-time
"""
#!python3

import sys
import os
os.system("cls")

inValue = input("Please enter any value: ")

print("\nThe given value is: ",inValue,end="\n")

if inValue:
    print("\nInput data identified you can proceed the business operations", end="\n")
else:
    print("\nInput data is missing, we cannot proceed.",end="\n")
    print("\nPlease confirm the end user is supplying the input definitely...",end="\n")
    
print("\nCurrently we are out of the \"IF\" branch, operating in the main stream of the program", end="\n")

"""
Scenario 02: Write a program to check given number is greater than 10 OR not.
"""
val01 = input("\nPlease enter any Numerical value: ")
print("\nThe given value is: ",val01,end="\n")

if int(val01)>10:
    print("The given value",val01, "is greater than 10",end="\n")
else:
     print("The given value",val01, "is less than 10",end="\n")

"""
Note:
-----
- When implementing branching we can do type conversion and then execute comparision.
- All comparision operators (ANSI: ==,!=, >,<,>=,<=) will operate only on numbers.
Errors:
-------
- The given value 10 is grater than 10  --> these type of errors called "Semantical OR logical errors"
- If we are not handled these errors properly, then they reflect as "bugs" in real-time implementation in the production environment.
"""

"""
Scenario 02: Write a program to check given number is an even number OR odd number
"""

value02 = int(input("\nPlease enter the Numerical number: "))

print("\nThe given number is: ",value02, end="\n")

if(value02 == 0 or value02 == 1):
    print("\nCannot determine the given number",value02,"is Even OR Odd state",end="\n")
    sys.exit()
    
if(value02 % 2 == 0):
    print("\nThe given input value", value02, "is Even",end="\n")
else:
    print("\nThe given input value", value02, "is Odd", end="\n")

    
"""
Nested if 
"""    
inVal = int(input("\nPlease enter any numeric number:"))
print("\nThe given number is:",inVal,end="\n")

if inVal >= 0:
    if inVal == 0:
        print("The given number is neither positive nor negative, the number is zero", inVal,end="\n")
    else:
        print("\nThe given number", inVal,"is: POSITIVE",end="\n")
else:
    print("\nThe given number",inVal, "is: NEGATIVE",end="\n")