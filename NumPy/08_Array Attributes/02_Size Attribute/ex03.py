#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.size attribute..",end="\n")

myArray = np.random.rand(200,200)

# print(f"\nThe given original array is..", end="\n")
# print(myArray)

print(f"\nThe current array size is: {myArray.size}", end="\n")

memoryUsed = myArray.size * myArray.itemsize

print(f"\nThe Total memory occupied by the arrray is: {memoryUsed} bytes", end="\n")

