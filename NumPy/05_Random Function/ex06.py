#! python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a single dimensional random float value....",end="\n")

outRandomNumber = np.random.rand()
print(f"\nThe generated single random float is: {outRandomNumber}", end="\n")

outRandomNumber01 = np.random.rand(5)
print(f"\nThe generated single random float is: {outRandomNumber01}", end="\n")

