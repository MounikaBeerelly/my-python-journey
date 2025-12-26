"""
Scenario:
---------
Write a program to find the GCD(Greatest Common Divisor) of a given two numbers
"""

import os
import sys
os.system("cls")

def findGCD(inParam01, inParam02) :
    """Function to calculate the GCD of two numbers"""
    if(inParam01 > inParam02) :
        tempStore = inParam02
    else:
        tempStore = inParam01
        
    for denoIndex in range(1, tempStore + 1) :
        if((inParam01 % denoIndex == 0) and (inParam02 % denoIndex == 0)) :
            gcdValue = denoIndex
    
    return gcdValue

inValue01 = int(input("\nPlease enter the first value: "))
inValue02 = int(input("\nPlease enter the second value: "))

gcdValue = findGCD(inValue01, inValue02)
        
print("\nThe GCD 0f %d and %d is %d" %(inValue01, inValue02, gcdValue), end="\n")
    
"""
Output:
-------

Please enter the first value: 56

Please enter the second value: 210

The GCD 0f 56 and 210 is 14

"""