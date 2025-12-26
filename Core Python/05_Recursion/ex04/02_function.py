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
    
    for raiseIndex in range(1, inValue + 1) :
        powerValue = powerValue * 10
    return powerValue

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
Please enter the number to raise 10 to the power of: 6

Calculating the power of 10 raised to a given number  6

The value 10 raised to the power of  6 is:  1000000
"""