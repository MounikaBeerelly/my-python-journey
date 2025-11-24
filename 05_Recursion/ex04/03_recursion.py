"""
Scenario:
---------
Write a program to find the power of 10, raised to a given number
"""

import os
import sys
os.system("cls")

def raiseTensPower(inParam) :
    """Function to calculate the 10 raised to given number"""
    powerValue = 1
    
    if inParam == 0:
        return 1
    
    return raiseTensPower(inParam - 1) * 10

inValue = int(input("\nPlease enter the number to raise 10 to the power of: "))

print("\nCalculating the power of 10 raised to a given number ", inValue, end="\n")

if inValue == 0 :
    sys.exit("\nThe power of 10 raised to 0 is: 1")
if inValue == 1 :
    sys.exit("\nThe power of 10 raised to 1 is: 10")
    
powerValue = raiseTensPower(inValue)

print("\nThe value 10 raised to the power of ", inValue, "is: ", powerValue, end="\n")
    
"""
Output:
-------
powerValuePlease enter the number to raise 10 to the power of: 3

Calculating the power of 10 raised to a given number  3

The value 10 raised to the power of  3 is:  1000
"""