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

"""
np.array()
----------
1. np.array() function is the primary method for creating NumPy arrays
2. np.array() converts python sequences like lists, tuples, or other array-like structures into NumPy arrays, which provide enhanced functionality of numerical computation

Basic Syntax:
-------------
numpy.array(object,dtype=none,copy=true,order='K',subok=False,ndmin=0)

Parameters Info:
----------------
1. Object: The input data(list,tuple,or other array-like object) to be converted into an array
2. dtype: (Optional) Specifies the desired data type for the array. If not provided, it is inferred from the input data
3. copy: (Optional) If true, creates a copy of the object. If False, a view of the object may be created
4. order: (optional) Specifies the memory layout. 'C' for row-major (c-style), 'F for column-major (Fortan-style), and 'K' for preserving the input order
5. subok: (Optional) If true, sub-classes of ndarray are passed through; otherwise, the base class is used
6. ndmin: (optional) specifies the minimum number of dimensions the array should have. If the input data has fewer dimensions, new axes are prepended.
"""
