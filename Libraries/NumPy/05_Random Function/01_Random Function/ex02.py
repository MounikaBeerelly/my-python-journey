#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a single dimensional array of random Flaot values..",end="\n")

inFloatCount = int(input("\nHow many elements you need in the array:"))

randomNumberArray = np.random.random(size = inFloatCount)
print(f"\nThe generated single dimensional random float array of '{inFloatCount}' Elements is: {randomNumberArray}",end="\n")
