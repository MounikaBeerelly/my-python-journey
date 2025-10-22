#! python3

import os
os.system("cls")
import numpy as np

myArray01 = np.array([1.25, 2.75, 3.63, 4.12, 5.87])

print(f"\nThe elements in the array is...", end="\n")
print(myArray01)

print(f"\nImplementig rounding operations upon the array of elements", end="\n")

# Round array
print(f"\nThe Rounded array is: {np.round(myArray01)}", end="\n")

# Ceil array
print(f"\nThe Ceiling array is: {np.ceil(myArray01)}", end="\n")

# Floor array
print(f"\nThe Floored array is: {np.floor(myArray01)}", end="\n")

