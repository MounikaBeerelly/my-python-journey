#!python3

import os
os.system("cls")

getValueLF = lambda inParam: inParam

inValue = int(input("\nPlease enter the value: "))

print("\nThe Reference address pointed by the \"Lambda\" function is : ", getValueLF, end="\n")
print("\nThe object ID of the \"lambda\" function is : ", id(getValueLF), end="\n")
print("\nThe Physical address of the \"Lambda\" function is : ", hex(id(getValueLF)), end="\n")
print("\nThe Type calss manages by the \"lambda\" function is : ", type(getValueLF), end="\n")
print("\nThe value referenced by the \"lambda\" function is : ", getValueLF(inValue), end="\n")

"""
Output:
-------
Please enter the value: 6

The Reference address pointed by the "Lambda" function is :  <function <lambda> at 0x000002469E58D940>

The object ID of the "lambda" function is :  2502327589184

The Physical address of the "Lambda" function is :  0x2469e58d940

The Type calss manages by the "lambda" function is :  <class 'function'>

The value referenced by the "lambda" function is :  6
"""