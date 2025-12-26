#! python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a a random value from a standard normal distribution (mean = 0, std = 1)....",end="\n")

myArrayValue = np.random.normal()
print(f"\nThe generated random value is: ",myArrayValue, end="\n")
