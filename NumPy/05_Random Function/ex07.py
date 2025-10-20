#! python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a Multi dimensional random float value....",end="\n")

outRandomNumber = np.random.rand(5,4)
print(f"\nThe generated array random float is...", end="\n")
print(outRandomNumber)
