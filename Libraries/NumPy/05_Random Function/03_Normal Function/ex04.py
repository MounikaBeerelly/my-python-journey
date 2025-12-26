#! python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a 3D array of random values from a normal distribution (mean = 0, std = 1)....",end="\n")

meanValue = 10
standardDeviation = 3
arrayShape = (3,4,5)

myArrayValues = np.random.normal(loc = meanValue, scale = standardDeviation, size = arrayShape)
print(f"\nThe generated 3D array with random values are..", end="\n")
print(myArrayValues)
