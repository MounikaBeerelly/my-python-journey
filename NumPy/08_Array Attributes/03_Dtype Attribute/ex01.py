#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.dtype attribute..",end="\n")

myArray = np.array([1,2,3,4,5])

print(f"\nThe given array is..", end="\n")
print(myArray)

print(f"\nThe current datatype of the array is: {myArray.dtype}", end="\n")