"""
Scenario:
---------
Write a program to find the GCD(Greatest Common Divisor) of a given two numbers
"""

import os
import sys
os.system("cls")

inValue01 = int(input("\nPlease enter the first value: "))
inValue02 = int(input("\nPlease enter the second value: "))

if inValue01 > inValue02 :
    tempStore = inValue02
else:
    tempStore = inValue01
    
for denoIndex in range(1, tempStore + 1) :
    if((inValue01 % denoIndex == 0) and (inValue02 % denoIndex == 0)) :
        gcdValue = denoIndex
        
print("\nThe GCD 0f %d and %d is %d" %(inValue01, inValue02, gcdValue), end="\n")
    
"""
Output:
-------
Please enter the first value: 12

Please enter the second value: 23

The GCD 0f 12 and 23 is 1
"""