#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a single dimensional array of random custom integer values...",end="\n")

inElementCount = int(input("\nHow many Elements you need in the array:"))

randomNumberArray = (np.random.random(size = inElementCount) * 100).astype(int)
print(f"\nThe generated Single dimensional Random Integer Array isn",end="\n")
print(f"\n{randomNumberArray}")