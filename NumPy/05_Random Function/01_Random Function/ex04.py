#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a Two dimensional array of random Flaot values by scaling the values..",end="\n")

inStartRange = int(input("\nGive the start range value of the array:"))
inEndRange = int(input("\nGive the end range value of the array:"))

print(f"\nThe given range of the values in the array is {inStartRange, inEndRange}",end="\n")

randomNumberArray = inStartRange + (inEndRange - inStartRange) * np.random.random(size = (2,3))
print(f"\nThe generated Two dimensional Random Float Array of order '2*3' Elements is\n",end="\n")
print(f"\n{randomNumberArray}")

inRowCount = int(input("\nHow many Rows you need in the array:"))
inColumnsCount = int(input("\nHow many columns you need in the array:"))

randomNumberArray01 = inStartRange + (inEndRange - inStartRange) * np.random.random(size = (inRowCount,inColumnsCount))
print(f"\nThe generated Two dimensional Random Float Array of order '{inRowCount} * {inColumnsCount}' Elements is\n",end="\n")
print(f"\n{randomNumberArray01}")