#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating An uninitialized array using numpy.empty()...",end="\n")

myArray01 = np.empty((3,4))
print(f"\nThe genereated empty array is..",end="\n")
print(myArray01)

myArray02 = np.empty((3,4), dtype=int)
print(f"\nThe genereated empty array is..",end="\n")
print(myArray02)