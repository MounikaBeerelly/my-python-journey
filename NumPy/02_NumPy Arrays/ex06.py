#!python3

import os
os.system("cls")
import numpy as np

print(f"\nCreating a single dimension array using list...",end="\n")

myArray01 = np.array([1,2,3,4,5],dtype=int)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray01)

myArray02 = np.array([6,7,8,9,10],dtype=int)
print(f"\nPrinting the elements from the array...",end="\n")
print(myArray01)

print(f"\ncombining two array into a final array..",end="\n")
finalArray = np.concatenate((myArray01,myArray02))
print(finalArray)