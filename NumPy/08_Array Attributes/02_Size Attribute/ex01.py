#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.size attribute..",end="\n")

myArray = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])

print(f"\nThe given array is..", end="\n")

print(myArray)

print(f"\nThe shape of the given array is: {myArray.shape}", end="\n")
print(f"\nThe size of the given array is: {myArray.size}", end="\n")
