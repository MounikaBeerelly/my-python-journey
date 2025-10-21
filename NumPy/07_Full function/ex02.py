#! python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a filled array using numpy.full()...",end="\n")

myArray01 = np.full((3,5), 2.5, dtype = float)
print(f"\nThe genereated full array is..",end="\n")
print(myArray01)