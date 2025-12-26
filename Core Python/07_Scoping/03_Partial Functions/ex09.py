#!python3

import os
os.system("cls")

from functools import partial

def raisePower(inBase, inExponent) :
    return inBase ** inExponent

raiseBaseTwo = partial(raisePower, 2)
raiseBaseThree = partial(raisePower, 3)
raiseBaseFour = partial(raisePower, 4)
raiseBaseFive = partial(raisePower, 5)
raiseBaseSix = partial(raisePower, 6)
raiseBaseSeven = partial(raisePower, 7)

inExponent = int(input("\nGive the exponent value: "))

print(f"2 raised to the power of {inExponent} is : {raiseBaseTwo(inExponent)}", end="\n")
print(f"3 raised to the power of {inExponent} is : {raiseBaseThree(inExponent)}", end="\n")
print(f"4 raised to the power of {inExponent} is : {raiseBaseFour(inExponent)}", end="\n")
print(f"5 raised to the power of {inExponent} is : {raiseBaseFive(inExponent)}", end="\n")
print(f"6 raised to the power of {inExponent} is : {raiseBaseSix(inExponent)}", end="\n")
print(f"7 raised to the power of {inExponent} is : {raiseBaseSeven(inExponent)}", end="\n")

"""
Output:
-------
Give the exponent value: 2
2 raised to the power of 2 is : 4
3 raised to the power of 2 is : 9
4 raised to the power of 2 is : 16
5 raised to the power of 2 is : 25
6 raised to the power of 2 is : 36
7 raised to the power of 2 is : 49
"""