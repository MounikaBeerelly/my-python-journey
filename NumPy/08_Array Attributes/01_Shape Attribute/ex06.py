#! python3

import os
os.system("cls")
import numpy as np

print(f"\nUnderstanding the ndarray.shape attribute..",end="\n")

my3DArray = np.random.randint(0,10,(2,3,4))

print(f"\nThe given array is..", end="\n")
print(my3DArray)

for myIndex in range(my3DArray.shape[0]):
    print(f"\nThe array slice {myIndex + 1} .. \n", my3DArray[myIndex])
    
    