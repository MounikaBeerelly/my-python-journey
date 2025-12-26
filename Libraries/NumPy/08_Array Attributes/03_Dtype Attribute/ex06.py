#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.dtype attribute..",end="\n")

print(f"\nUnderstanding the precision of the array by using dtype parameter")
myArrayFloat32 = np.array([1.123456789], dtype = 'float32')
myArrayFloat64 = np.array([1.123456789], dtype = 'float64')

print(f"\nThe float32 array is..", end="\n")
print(myArrayFloat32)

print(f"\nThe float64 array is..", end="\n")
print(myArrayFloat64)
