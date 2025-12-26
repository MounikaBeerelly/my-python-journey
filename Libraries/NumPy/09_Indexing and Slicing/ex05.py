#! python3

import os
os.system("cls")
import numpy as np

myArray01 = np.array([1,2,3,4,5])
myArray02 = np.array([6,7,8,9,10])

print(f"\nThe given first array: {myArray01}", end="\n")
print(f"\nThe given second array : {myArray02}", end="\n")

print(f"\nSubtracting the elements of both the arrays...", end="\n")
finalArray = myArray02 - myArray01

print(f"\nThe Array 02 {myArray02} subtracted from Array 01 {myArray01} is: {finalArray}", end="\n")

