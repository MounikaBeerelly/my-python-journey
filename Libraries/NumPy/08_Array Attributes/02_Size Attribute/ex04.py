#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.shape attribute..",end="\n")

myArray = np.array([1,2,3,4,5,6,7,8])

print(f"\nThe given array is..", end="\n")

print(myArray)

if myArray.size == 0:
    print(f"\nThe given array is empty..", end="\n")
else:
    print(f"\nThe given array is loaded with elements..", end="\n")