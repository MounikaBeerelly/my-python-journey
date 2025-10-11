#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating an array from another array..",end="\n")

myArrayInt01 = np.array([1,2,3,4,5], dtype=int)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArrayInt01)

myArrayFloat01 = np.array(myArrayInt01, dtype=float)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArrayFloat01)