#!python3

import os
os.system("cls")
import numpy as np

print(f"\nGenerating a Two dimensional array of random Flaot values using Reshaping concept..",end="\n")

inRowCount = int(input("\nHow many Rows you need in the array:"))
inColumnsCount = int(input("\nHow many columns you need in the array:"))

print(f"\nThe total elements in the array will be: {inRowCount,inColumnsCount}",end="\n")

randomNumberArray = np.random.random(size = (inRowCount,inColumnsCount))
print(f"\nThe generated Two dimensional Random Float Array of order '{inRowCount} * {inColumnsCount}' Elements is\n",end="\n")
print(f"\n{randomNumberArray}")
