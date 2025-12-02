#!python3

import os
os.system("cls")

def getSum(inParam01) :
    def calSum(inParam02) :
        return inParam01 + inParam02
    return calSum

if __name__ == "__main__" :
    inValue01 = int(input("\nPlease enter the first value: "))
    closureFunction = getSum(inValue01)
    
    for loopIndex in range(10) :
        print("\nThe sum of %d and %d is: %d"%(inValue01, loopIndex, closureFunction(loopIndex)))
    

"""
Output:
-------

Please enter the first value: 26

The sum of 26 and 0 is: 26

The sum of 26 and 1 is: 27

The sum of 26 and 2 is: 28

The sum of 26 and 3 is: 29

The sum of 26 and 4 is: 30

The sum of 26 and 5 is: 31

The sum of 26 and 6 is: 32

The sum of 26 and 7 is: 33

The sum of 26 and 8 is: 34

The sum of 26 and 9 is: 35
"""
    