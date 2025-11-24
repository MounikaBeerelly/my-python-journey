"""
Scenario:
---------
Write a program to find the GCD(Greatest Common Divisor) of a given two numbers
"""

import os
import sys
os.system("cls")

def findGCD(inParam01, inParam02) :
    """Function to find the GCD of two numbers"""
    if(inParam01 == inParam02) :
        return inParam01
    elif (inParam01 > inParam02):
        nextVal = inParam01 - inParam02
       # currGCD = findGCD(inParam01 - inParam02, inParam02)
        currGCD = findGCD(nextVal, inParam02)
        return currGCD
    else : 
        nextVal = inParam02 - inParam01
        # currGCD = findGCD(inParam01, inParam02 - inParam01)
        currGCD = findGCD(inParam01, nextVal)
        return currGCD

inValue01 = int(input("\nPlease enter the first value: "))
inValue02 = int(input("\nPlease enter the second value: "))

gcdValue = findGCD(inValue01, inValue02)
        
print("\nThe GCD 0f %d and %d is %d" %(inValue01, inValue02, gcdValue), end="\n")
    
"""
Output:
-------
Please enter the first value: 54

Please enter the second value: 12

The GCD 0f 54 and 12 is 6
"""