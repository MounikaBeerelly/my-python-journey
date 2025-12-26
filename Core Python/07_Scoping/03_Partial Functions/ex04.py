#!python3

import os
os.system("cls")

def getMultipler(inParam01, inMultipleValue) :
    return inParam01 * inMultipleValue

if __name__ == "__main__" :
    print("\n1. Double the value\n2. Triple the value\n3. Quadraple the value\n4. Pentaple the value\n0. Exit the application", end="\n")
    readChoice = int(input("\nPlease enter your choice: "))
    inValue01 = int(input("\nPlease enter the value: "))
    
    if readChoice == 1 :
        finalValue = getMultipler(inValue01, 2)
        print("\nThe given value for applying Doubler is: %d" %(inValue01), end="\n")
        print("\nThe result of %d when doubled is: %d"%(inValue01, finalValue), end="\n")
    elif readChoice == 2:
        finalValue = getMultipler(inValue01, 3)
        print("\nThe given value for applying Tripler is: %d" %(inValue01), end="\n")
        print("\nThe result of %d when tripled is: %d"%(inValue01, finalValue), end="\n")
    elif readChoice == 3:
        finalValue = getMultipler(inValue01, 4)
        print("\nThe given value for applying Quadrapler is: %d" %(inValue01), end="\n")
        print("\nThe result of %d when Quadrapled is: %d"%(inValue01, finalValue), end="\n")
    elif readChoice == 4:
        finalValue = getMultipler(inValue01, 5)
        print("\nThe given value for applying Pentapler is: %d" %(inValue01), end="\n")
        print("\nThe result of %d when Pentapled is: %d"%(inValue01, finalValue), end="\n")
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

Please enter your choice: 4

Please enter the value: 6

The given value for applying Pentapler is: 6

The result of 6 when Pentapled is: 30
"""