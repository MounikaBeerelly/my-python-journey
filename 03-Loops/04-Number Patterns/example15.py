"""
Generate number pattern like below:
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5
"""

import os
os.system("cls")

rowRange = int(input("Please enter the number of rows to be generated:"))

rowIndex = 1

print()

while(rowIndex <= rowRange):
    columnIndex = rowIndex
    while(columnIndex < rowRange):
        print(" ",end="")
        columnIndex += 1
        
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print("%d"%(columnIndex), end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()