#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a filled array using numpy.full()...",end="\n")

myArray01 = np.full(5,0)
print(f"\nThe genereated full array is..",end="\n")
print(myArray01)
  
myArray02 = np.full((5,5),5)
print(f"\nThe genereated full array is..",end="\n")
print(myArray02)    

myArray03 = np.full((5,5,3),4)
print(f"\nThe genereated full array is..",end="\n")
print(myArray03)          