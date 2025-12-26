#! python3

import os
os.system("cls")
import numpy as np

myArray01 = np.array([
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ])

print(f"\nThe elements in the first array...", end="\n")
print(myArray01)

myArray02 = np.array([
                        [6, 2, 4],
                        [9, 1, 3],
                        [5, 2, 8]
                    ])

print(f"\nThe elements in the second array...", end="\n")
print(myArray02)

print(f"\nImplementing matrix addition...",end="\n")
sumOfArrays = myArray01 + myArray02
print(f"\nThe sum of array is...", end="\n")
print(sumOfArrays)

print(f"\nImplementing matrix subtraction...",end="\n")
subtractionOfArrays = myArray02 - myArray01
print(f"\nThe subtraction of array is...", end="\n")
print(subtractionOfArrays)

print(f"\nImplementing matrix multiplication...",end="\n")
multiplicationOfArrays = np.dot(myArray01, myArray02)
#multiplicationOfArrays = myArray01 @ myArray02
print(f"\nThe multiplication array is...", end="\n")
print(multiplicationOfArrays)

print(f"\nImplementing Element wise matrix multiplication...",end="\n")
multiplicationOfArrays1 = myArray01 * myArray02
print(f"\nThe multiplication array is...", end="\n")
print(multiplicationOfArrays1)