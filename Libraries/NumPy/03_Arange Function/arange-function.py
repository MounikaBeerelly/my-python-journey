#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a single dimension array using arange function...",end="\n")

myArray01 = np.arange(10)
print(f"\nPrinting the elements from the array01...",end="\n")
print(myArray01)

myArray02 = np.arange(5,15)
print(f"\nPrinting the elements from the array02...",end="\n")
print(myArray02)

myArray03 = np.arange(0,15,2)
print(f"\nPrinting the elements from the array03...",end="\n")
print(myArray03)

myArray04 = np.arange(0,10,dtype=float)
print(f"\nPrinting the elements from the array04...",end="\n")
print(myArray04)

myArray05 = np.arange(0,10,0.1,dtype=float)
print(f"\nPrinting the elements from the array05...",end="\n")
print(myArray05)

myArray06 = np.arange(0,10,dtype=float)
print(f"\nPrinting the elements from the array06...",end="\n")
print(myArray06)

myArray07 = np.arange(0,1,0.1)
print(f"\nPrinting the elements from the array07...",end="\n")
print(myArray07)

myArray08 = np.arange(10,0,-1)
print(f"\nPrinting the elements from the array08...",end="\n")
print(myArray08)

myArray09 = np.arange(10,1)
print(f"\nPrinting the elements from the array09...",end="\n")
print(myArray09)
