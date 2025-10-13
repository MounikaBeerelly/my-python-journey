#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a single dimension array of 1*5 oder filled with zeros..",end="\n")

myArray = np.zeros((1,5))
print(f"\nPrinting the elements from the array..",end="\n")
print(myArray)

print(f"\nCreating a two dimension array of 2*5 oder filled with zeros..",end="\n")

myArray01 = np.zeros((2,5))
print(f"\nPrinting the elements from the array..",end="\n")
print(myArray01)

print(f"\nCreating a multi dimension array of 3*5 oder filled with ones..",end="\n")

myArray02 = np.ones((3,5))
print(f"\nPrinting the elements from the array..",end="\n")
print(myArray02)