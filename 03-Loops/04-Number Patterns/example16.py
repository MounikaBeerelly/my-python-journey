"""
Generate number pattern like below:
 5 5 5 5 5
  4 4 4 4
   3 3 3
    2 2
     1
"""

import os
os.system("cls")

rowRange = int(input("Please enter the number of rows to be generated:"))

rowIndex = rowRange

print()

while(rowIndex >= 1):
    columnIndex = rowRange
    while(columnIndex > rowIndex):
        print(" ",end="")
        columnIndex -= 1
        
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print("%d"%(rowIndex), end=" ")
        columnIndex += 1
    
    rowIndex -= 1
    print()