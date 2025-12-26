#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.dtype attribute..",end="\n")

myArray = np.array([1,2,3,4,5])

if myArray.dtype == np.int32:
    print(f"\nThe given array is..", end="\n")
    print(myArray)
else:
    print(f"\nSorry! Given array is not compatible type", end="\n")