"""
Scenario: Write a program to find the given value is positive/negative
"""

import os
import sys
os.system("cls")

try :
    inValue = int(input("\nPlease enter a value : "))

    if inValue < 0 :
        raise ValueError("Hey! the given value is Negative, cannot continue")
    else :
        print("\nThe value entered is Positive OR Zero", end="\n")
        print("\nThe given value is : ", inValue, end="\n")
except ValueError as valueErrorObj :
    print("\nIn-valid input detected! please provide a valid integer..", end = "\n")
    print("\nMessage from Interpretor is : ", valueErrorObj, end="\n")
    sys.exit("\nProgram Terminated due to an Error...")
except BaseException as baseExcepObj :
    print("\nHey! Un known abnormality identified, the final exceptional message is : ",baseExcepObj, end="\n")

"""
Output:
------

Please enter a value : -6

In-valid input detected! please provide a valid integer..

Message from Interpretor is :  Hey! the given value is Negative, cannot continue

Program Terminated due to an Error...
"""