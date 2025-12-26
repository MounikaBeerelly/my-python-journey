#!python3

import os
os.system("cls")

def valueDoubler(inParam01) :
    print("\nThe given values for applying Doubler is: %d" %(inParam01), end="\n")
    return inParam01 + inParam01

if __name__ == "__main__" :
    inValue01 = int(input("\nPlease enter the value to be doubled: "))
    finalValue = valueDoubler(inValue01)
    print("\nThe result of %d when doubled is: %d"%(inValue01, finalValue), end="\n")
    
    
"""
Output:
-------
Please enter the value to be doubled: 16

The given values for applying Doubler is: 16

The result of 16 when doubled is: 32
"""