#! python3

import os
os.system("cls")
import numpy as np

temparatureData = np.array([22.5, 24.0, 23.8, 25.3, 26.1, 27.0, 23.5])

print(f"\nThe recorded temparatures in this week: {temparatureData}", end="\n")

inStartIndex = int(input("\nPlease enter the starting index to slice : "))
inEndIndex = int(input("\nPlease enter the ending index to slice : "))

print(f"\nThe original recorded temperatures are : {temparatureData}", end="\n")

print(f"\nThe values sliced starting from {inStartIndex} to {inEndIndex} are: {temparatureData[inStartIndex : inEndIndex]}", end="\n")
