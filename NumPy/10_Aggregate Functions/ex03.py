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

# Transposing of the matrix
print(f"\nImplementing transposing of the matrix elements...", end="\n")
transposeArray = myArray01.T
print(f"\nThe final array is...", end="\n")
print(transposeArray)

# Determinant of the matrix
print(f"\nImplementing determinant of the matrix elements...", end="\n")
determinantArray = np.linalg.det(myArray01)
print(f"\nThe final array is...", end="\n")
print(determinantArray)

# Inverse of a matrix
print(f"\nImplementing inverse of the matrix...",end="\n")
if determinantArray == 0:
    print(f"\nSorry! normal Inverse cannot be implemented, as determinant is zero", end="\n")
    print(f"\nImplementing Pseudo Inverse upon the matrix...", end="\n")
    pseudoInverse = np.linalg.pinv(myArray01)
    print(f"\nThe pseudo inverse of the matrix is...", end="\n")
    print(pseudoInverse)
else:
    inverseArray = np.linalg.inv(myArray01)
    print(f"\nthe final array is...", end="\n")
    print(inverseArray)
    
# Trace of a matrix
print(f"\nImplementing th etrace of a matrix...", end="\n")

traceArray = np.trace(myArray01)

print(f"\nThe trace of the array is..", end="\n")
print(traceArray)