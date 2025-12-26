#!python3

import os
os.system("cls")

def valueDoubler(inParam01) :
    print("\nThe given value for applying Doubler is: %d" %(inParam01), end="\n")
    return inParam01 + inParam01

def valueTripler(inParam01) :
    print("\nThe given value for applying Tripler is: %d" %(inParam01), end="\n")
    return inParam01 + inParam01 + inParam01

def valueQuadrapler(inParam01) :
    print("\nThe given value for applying Quadrapler is: %d" %(inParam01), end="\n")
    return inParam01 + inParam01 + inParam01 + inParam01

def valuePentapler(inParam01) :
    print("\nThe given value for applying Pentapler is: %d" %(inParam01), end="\n")
    return inParam01 + inParam01 + inParam01 + inParam01 + inParam01

if __name__ == "__main__" :
    print("\n1. Double the value\n2. Triple the value\n3. Quadraple the value\n4. Pentaple the value\n0. Exit the application", end="\n")
    readChoice = int(input("\nPlease enter your choice: "))
    inValue01 = int(input("\nPlease enter the value: "))
    
    if readChoice == 1 :
        finalValue = valueDoubler(inValue01)
        print("\nThe result of %d when doubled is: %d"%(inValue01, finalValue), end="\n")
    elif readChoice == 2:
        finalValue = valueTripler(inValue01)
        print("\nThe result of %d when tripled is: %d"%(inValue01, finalValue), end="\n")
    elif readChoice == 3:
        finalValue = valueQuadrapler(inValue01)
        print("\nThe result of %d when Quadrapled is: %d"%(inValue01, finalValue), end="\n")
    elif readChoice == 4:
        finalValue = valuePentapler(inValue01)
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

Please enter your choice: 3

Please enter the value: 3

The given value for applying Quadrapler is: 3

The result of 3 when Quadrapled is: 12

"""