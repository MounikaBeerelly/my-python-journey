#!python3

import os
os.system("cls")

from functools import partial

def applyMultipler(inParam01, inMultipleValue) :
    return inParam01 * inMultipleValue

if __name__ == "__main__" :
    print("\n1. Double the value\n2. Triple the value\n3. Quadraple the value\n4. Pentaple the value\n0. Exit the application", end="\n")
    readChoice = int(input("\nPlease enter your choice: "))
    inValue01 = int(input("\nPlease enter the value: "))
    
    if readChoice == 1 :
        finalValue = partial(applyMultipler, 2)
        print(finalValue)
        print("\nThe result of %d when doubled is: %d"%(inValue01, finalValue(inValue01)), end="\n")
    elif readChoice == 2:
        finalValue = partial(applyMultipler, 3)
        print("\nThe result of %d when tripled is: %d"%(inValue01, finalValue(inValue01)), end="\n")
    elif readChoice == 3:
        finalValue = partial(applyMultipler, 4)
        print("\nThe result of %d when Quadrapled is: %d"%(inValue01, finalValue(inValue01)), end="\n")
    elif readChoice == 4:
        finalValue = partial(applyMultipler, 5)
        print("\nThe result of %d when Pentapled is: %d"%(inValue01, finalValue(inValue01)), end="\n")
    else:
        print("\nYou chose the application to Quit", end="\n")
    
"""
Output:
-------
1. Double the value
2. Triple the value
3. Quadraple the value
4. Pentaple the value
0. Exit the application

Please enter your choice: 3

Please enter the value: 8

The result of 8 when Quadrapled is: 32
"""