#!python3
 
import os
os.system("cls")

inValue = int(input("\nPlease give any integer value : "))

try : 
    assert inValue > 0, "Given value is Negative, cannot continue operations"
    print("\nHey! found a positive number", end="\n")
except AssertionError as assertExceptObj :
    print("\nAssertion failed.. Cannot continue..", end="\n")
    print("\nThe identified exception is : ", assertExceptObj, end="\n")
except BaseException as baseExcepObj :
    print("\nHey! Un known abnormality identified, the final exception message is: ", baseExcepObj, end="\n")
"""
Output:
------
Please give any integer value : -9

Assertion failed.. Cannot continue..

The identified exception is :  Given value is Negative, cannot continue operations
"""