#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.size attribute..",end="\n")

myArray = np.arange(12)

print(f"\nThe given original array is..", end="\n")
print(myArray)

print(f"\nThe current array size is: {myArray.size}", end="\n")

reshapeArray = myArray.reshape(3,4)

print(f"\nThe reshaped array is...", end="\n")
print(reshapeArray)

print(f"\nThe reshaped array size id: {reshapeArray.size}", end="\n")
