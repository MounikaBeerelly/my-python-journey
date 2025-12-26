#! python3

import os
os.system("cls")
import numpy as np

def checkArrayCompatibility(inArray01, inArray02):
    """Function to check whether the given arrays are compatible OR not"""
    return inArray01.shape == inArray02.shape

print(f"\nUnderstanding the ndarray.shape attribute..",end="\n")

myArray01 = np.array([[1,2,3],[4,5,6],[7,8,9]])
myArray02 = np.array([[10,11,12],[13,14,15],[16,17,18]])

print(f"\nThe given array 01 is..", end="\n")
print(myArray01)

print(f"\nThe given array 02 is..", end="\n")
print(myArray02)

if checkArrayCompatibility(myArray01,myArray02):
    print(f"\nThe given arrays are compatible in shape..", end="\n")
else:
    print(f"\nThe given arrays are not compatible in shapes..", end="\n")