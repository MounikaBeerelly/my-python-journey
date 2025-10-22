#! python3

import os
os.system("cls")
import numpy as np

imageIndexes = np.array([
                        [255, 200, 150, 120, 100],
                        [230, 210, 180, 130, 160],
                        [180, 170, 160, 140, 120],
                        [140, 130, 120, 110, 100],
                        [100, 90, 80, 70, 60]
                    ])
print(f"\nThe pixels tracked in the image are..", end="\n")
print(imageIndexes)

rowIndex = int(input("\nPlease enter the row value to extract the pixel values:"))
columnIndex = int(input("\nPlease enter the cloumn value to extract the pixel values:"))

pixelValue = imageIndexes[rowIndex-1, columnIndex-1]

print(f"\nThe identified pixel value at row {rowIndex} and column {columnIndex} is : {pixelValue}", end="\n")