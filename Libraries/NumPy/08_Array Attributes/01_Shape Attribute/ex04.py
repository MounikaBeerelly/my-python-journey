#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.shape attribute..",end="\n")

myArray = np.array([1,2,3,4,5,6,7,8])

print(f"\nThe given array is..", end="\n")

print(myArray)

if myArray.size == 2 * 4:
    myArray.shape = (2,4)
    print(f"\nPrinting the reshaped array is..", end="\n")
    print(myArray)
else:
    print(f"\nReshaping the current array is not possible..", end="\n")