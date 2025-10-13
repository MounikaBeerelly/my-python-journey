#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a Single dimension array using linspace function in integration with reshape() function...",end="\n")

myArray01 = np.linspace(0,1,10)
print(f"\nPrinting the elements from the array01...",end="\n")
print(myArray01)

myArray02 = np.linspace(0,10,5)
print(f"\nPrinting the elements from the array03...",end="\n")
print(myArray02)

myArray03 = np.linspace(0,10,5, endpoint=False)
print(f"\nPrinting the elements from the array03...",end="\n")
print(myArray03)

myArray04,stepValue = np.linspace(0,10,5, retstep=True)
print(f"\nPrinting the elements from the array04...",end="\n")
print(myArray04)
print(f"\nThe step value fixed is: {stepValue}",end="\n")

myArray05 = np.linspace(0,10,5, dtype=int)
print(f"\nPrinting the elements from the array05...",end="\n")
print(myArray05)
"""
Generated Output:
----------------
Printing the elements from the array01...
[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]
 
1. The np.linspace() function in NumPy generates evenly spaced values between a specified start and stop value over a defined number of points.
2. np.linspace() focuses on the number of points and ensures equal spacing

Basic Syntax:
------------
numpy.linspace(start,stop,num=50, endpoint=True, restep=False, dtype=none, axis=0)

start: The starting value of the sequence
stop: The ending value of the sequence
num: (Optional) The number of points to generate. Default is 50
endpoint: (Optional) If true (default), includes the stop value; otherwise, excludes it
retstep: (Optional) If True, returns the spacing between points along with the array
dtype: (Optional) specifies the desired data type of the output array
axis: (Optional) Axis in the result along which the values are stored

Where to use?
-------------
1. Ideal for generating fixed-size arrays with precise spacing
2. Ensures the array covers the specified range with or without including the stop value
"""

