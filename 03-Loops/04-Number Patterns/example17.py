"""
Generate number pattern which points the sequence of numbers as specified for the range of the rows, printing the generating sequence advance by one value of each row:
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))
columnRange = int(input("Please enter the number of columns to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = rowIndex
    while(columnIndex < (columnRange+rowIndex)):
        print("%d"%(columnIndex), end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()