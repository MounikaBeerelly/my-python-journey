#! python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating an array of 10 random value from a normal distribution (mean = 0, std = 1)....",end="\n")

myArrayValues = np.random.normal(loc = 5, scale = 2, size = 10)
print(f"\nThe generated array with random values are..", end="\n")
print(myArrayValues)
