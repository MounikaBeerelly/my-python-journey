#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a Two dimension array using linspace function in integration with reshape() function...",end="\n")

myArray01 = np.linspace(1,12,12)
print(f"\nPrinting the elements from the array01...",end="\n")
print(myArray01)

myArray02 = np.linspace(1,12,12).reshape(3,4)
print(f"\nPrinting the elements from the array02...",end="\n")
print(myArray02)

