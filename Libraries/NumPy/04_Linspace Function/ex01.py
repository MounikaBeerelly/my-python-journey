#!python3

import os
os.system("cls")
import numpy as np

# Single dimension array
print(f"\nCreating a single dimension array using list...",end="\n")

myArrayInt01 = np.linspace(1,12,12)
print(f"\nPrinting the elements from the array..",end="\n")
print(myArrayInt01)

# converting linearspace to non-linear space
myArrayInt02 = np.linspace(1,12,12)
logArray = np.log(myArrayInt02)
print(f"\nPrinting the elements from the array..",end="\n")
print(logArray)