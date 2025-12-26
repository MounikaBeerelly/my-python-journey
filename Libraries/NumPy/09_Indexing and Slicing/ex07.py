#! python3

import os
os.system("cls")
import numpy as np

myArray01 = np.array([1,2,3,4,5])

print(f"\nThe given array: {myArray01}", end="\n")

productValue = int(input("\nPlease enter the value to be used for multiplying the array elements:"))

print(f"\nMultiplying the elements of an array by {productValue}", end="\n")
finalArray = myArray01 * productValue

print(f"\nThe final array is: {finalArray}", end="\n")

