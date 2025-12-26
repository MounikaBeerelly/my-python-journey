import os
os.system("cls")

import traceback

def executeDivision(inNumerator, inDenominator) :
    try :
        quotientValue = inNumerator / inDenominator
        return quotientValue
    except ZeroDivisionError as zeroDivideErrorObj :
        traceback.print_exc()
        return None
    
inNumerator = int(input("\nPlease enter the Numerator value : "))
inDenominator = int(input("\nPlease enter the Denominator value : "))

outResult = executeDivision(inNumerator, inDenominator)

if outResult is None :
    print("\nFatal error! Division by zero occured..", end="\n")
else:
    print("\nThe calculated quotient is : ", outResult, end="\n")
    
      
"""
Output:
-------

Please enter the Numerator value : 12

Please enter the Denominator value : 0
Traceback (most recent call last):
  File "C:\Practice\my-python-journey\09_Exceptions\Traceback\ex03.py", line 8, in executeDivision
    quotientValue = inNumerator / inDenominator
ZeroDivisionError: division by zero

Fatal error! Division by zero occured..
"""