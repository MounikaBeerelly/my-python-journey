#! python3

import os
os.system("cls")
import numpy as np

myArray01 = np.array([1, 2, 3, 4, 5])

print(f"\nThe elements in the array is...", end="\n")
print(myArray01)

print(f"\nImplementig Shape Manipulation, by expanding the matrix", end="\n")

# expanding array
expandedArray = np.expand_dims(myArray01, axis = 0)

print(f"\nThe expanded array is..", end="\n")
print(expandedArray)

# squeezing array
squeezedArray = np.squeeze(expandedArray)

print(f"\nThe squeezed array is..", end="\n")
print(squeezedArray)
