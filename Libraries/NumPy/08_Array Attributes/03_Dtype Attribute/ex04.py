#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.dtype attribute..",end="\n")

myArray = np.array([1.1,2.2,3.3,4.4,5.5], dtype = 'float64')

print(f"\nThe given array is..", end="\n")
print(myArray)

myArrayInt = myArray.astype('int32')

print(f"The converted array is...", end="\n")
print(myArrayInt)
print(f"\nThe converted array datatype is: {myArrayInt.dtype}", end="\n")