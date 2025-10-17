#!python3

import os
os.system("cls")
import numpy as np

# Single dimension array
print(f"\nCreating a single dimension array using list...",end="\n")

myArrayInt01 = np.array([1,2,3,4,5])
print(f"\nPrinting the elements from the array...",end="\n")
print(myArrayInt01)

myArrayFloat01 = np.array([1.2, 2.3, 3.4, 4.5, 5.6])
print(f"\nPrinting the elements from the array...",end="\n")
print(myArrayFloat01)

myArrayInt02 = np.array([1.2, 2.3, 3.4, 4.5, 5.6], dtype= int)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArrayInt02)

myArrayFloat02 = np.array([1,2,3,4,5], dtype=float)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArrayFloat02)

myArraycomplex = np.array([1,2,3,4,5], dtype=complex)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArraycomplex)

myArray2D = np.array([1,2,3,4,5], ndmin = 2)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray2D)

myArray3D = np.array([1,2,3,4,5], ndmin = 3)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray3D)
