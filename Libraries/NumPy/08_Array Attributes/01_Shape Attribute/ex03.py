#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.shape attribute..",end="\n")

myArray = np.array([1,2,3,4,5,6])

print(f"\nThe given array is..", end="\n")

print(myArray)

myArray.shape = (2,3)

print(f"\nPrinting the reshaped array is..", end="\n")

print(myArray)