#! python3

import os
os.system("cls")
import numpy as np

myArray01 = np.array([1, 2, 3, 4, 5, 6, 2, 5, 7, 8, 3, 2, 9])

print(f"\nThe elements in the array is...", end="\n")
print(myArray01)


print(f"\nImplementing Rounding operations upon the array elements", end="\n")

uniqueValues, elementCounts = np.unique(myArray01, return_counts = True)

print(f"\nThe unique values in the array {uniqueValues}", end="\n")
print(f"\nThe count of each element in the array: {elementCounts}", end="\n")