#!python3

import os
os.system("cls")

def applyMultiple(inParam01, inParam02) :
    print("\nThe given values for applying multiplier are: %d, %d" %(inParam01, inParam02), end="\n")
    return inParam01 * inParam02

if __name__ == "__main__" :
    inValue01 = int(input("\nPlease enter the value to be multiplied: "))
    inValue02 = int(input("\nPlease enter the value of Multipler: "))
    finalValue = applyMultiple(inValue01, inValue02)
    print("\nThe result of %d multiplied by %d is: %d"%(inValue01, inValue02, finalValue), end="\n")
    
    
"""
Output:
-------
Please enter the value to be multiplied: 23

Please enter the value of Multipler: 12

The given values for applying multiplier are: 23, 12

The result of 23 multiplied by 12 is: 276
"""