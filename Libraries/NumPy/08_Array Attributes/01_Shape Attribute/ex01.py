#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.shape attribute..",end="\n")

myArray = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])

print(f"\nThe given array is..", end="\n")

print(myArray)

print(f"\nThe shape of the given array is: {myArray.shape} order", end="\n")

outRows, outColumns = myArray.shape

print(f"\nThe number of Rows in the given array are: {outRows} rows", end="\n")
print(f"\nThe number of columns in the given array are: {outColumns} columns", end="\n")