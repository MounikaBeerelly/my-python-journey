"""
Generate number pattern like below:
1
22
333
4444
55555
"""

import os
os.system("cls")

rowRange = int(input("Please enter the number of rows to be generated:"))

rowIndex = 1

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print("%2d"%(rowIndex), end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()