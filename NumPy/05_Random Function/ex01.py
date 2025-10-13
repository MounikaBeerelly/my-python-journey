"""
1. The np.random.random() function generates random floating-point numbers uniformly distributed between 0.0 (inclusive) and 1.0 (exclusive)
2. The random numbers are drawn from a uniform distribution and are useful for
    1. Simulations
    2. Testing
    3. Creating random datasets

Basic Syntax:
-------------
np.random.random(size = none)

1. size: Specifies the shape of the output array
    1. If None (default), a single flaot is returned
    2. If an integer is provided, a 1D array of that length is returned
    3. If a tuple is provided, it creates an array with the specified shape
    
2. np.random.random() part of NumPy's random module, which provides a suite of random number generation functions

"""

#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a single random Flaot value..",end="\n")

outRandomNumber = np.random.random()
print(f"\nThe generating single floating point value is: {outRandomNumber}",end="\n")
