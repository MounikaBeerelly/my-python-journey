#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.dtype attribute..",end="\n")

myArray8Bit = np.array([1,2,3,4,5], dtype = 'int8')

print(f"\nThe given array is..", end="\n")
print(myArray8Bit)

myArray64Bit = np.array([1,2,3,4,5], dtype = 'int64')

print(f"\nThe given array is..", end="\n")
print(myArray64Bit)

print(f"\nThe sizr of the int8 array is: {myArray8Bit.dtype} bytes", end="\n")
print(f"\nThe size of the int64 array is: {myArray64Bit.dtype} bytes", end="\n")