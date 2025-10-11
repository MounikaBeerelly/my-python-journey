#!python3

import os
os.system("cls")
import numpy as np

# Single dimension array
print(f"\nCreating a single dimension array of 1*5 oder using tuple...",end="\n")

myArray = np.array((1,2,3,4,5))
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray)

# two dimension array
print(f"\nCreating a two dimension array of 2*5 oder using tuple...",end="\n")

myArray1 = np.array(((1,2,3,4,5),(6,7,8,9,10)))
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray1)

# multi dimension array
print(f"\nCreating a multi dimension array of 3*5 oder using tuple...",end="\n")

myArray2 = np.array(((1,2,3,4,5),(6,7,8,9,10),(11,12,13,14,15)))
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray2)