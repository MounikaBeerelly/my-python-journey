"""
Generating a Inverted hollow right angle triangle pattern, given the number of rows
* * * * *
*     *
*   *
* *
*
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = rowIndex
    while(columnIndex <= rowRange):
        if(rowIndex == 1 or columnIndex == rowIndex or columnIndex == rowRange):
            print("*",end=" ")
        else:
            print(" ", end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()
    