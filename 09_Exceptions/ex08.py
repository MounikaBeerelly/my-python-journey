import os
os.system("cls")

print("\nModule to operate Division process", end="\n")

inNumerator = int(input("\nPlease enter the Numerator value : "))
inDenominator = int(input("\nPlease enter the Denominator value : "))

print("\nExecuting the division operation without validating the Denomination", end="\n")
try :
    quotientValue = inNumerator / inDenominator
    print("\nThe Quotient of %0.2f and %0.2f is : %0.2f"%(inNumerator, inDenominator, quotientValue), end="\n")
except ZeroDivisionError as zeroDivObj :
    print("\nSorry! Denominator cannot be : Zero", end="\n")
    print("\nExecution of the Division is cancelled.. terminating the module..", end="\n")
    print("\nThe Interpretor response is : ", zeroDivObj, end="\n")
except BaseException as baseExcepObj :
    print("\nFatal! Un-Identified exception is encountered...", end="\n")
    print("The generic exception calss is identified with : ", baseExcepObj, end="\n")
    print("\nPlease debug the module for more specific identification of the exception state...", end="\n")
else :
    print("\nGiven operation is successfully executed", end="\n")
finally :
    print("\nResources De-Allocation section operating always finally when leaving the exception section", end="\n")
    
"""
Output:
-------
-------------- Output 01: ------------
Module to operate Division process

Please enter the Numerator value : 34

Please enter the Denominator value : 2

Executing the division operation without validating the Denomination

The Quotient of 34.00 and 2.00 is : 17.00

Given operation is successfully executed

Resources De-Allocation section operating always finally when leaving the exception section

-----------Output 02:----------------

Module to operate Division process

Please enter the Numerator value : 12

Please enter the Denominator value : 0

Executing the division operation without validating the Denomination

Sorry! Denominator cannot be : Zero

Execution of the Division is cancelled.. terminating the module..

The Interpretor response is :  division by zero

Resources De-Allocation section operating always finally when leaving the exception section

"""