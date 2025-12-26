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
    inValue02 = int(input("\nPlease enter the second value: "))
    print("\nThe sum of %d and %d is: %d"%(inValue01, inValue02, closureFunction(inValue02)))
    

"""
Output:
-------
Please enter the first value: 23

Please enter the second value: 43

The sum of 23 and 43 is: 66
"""
    