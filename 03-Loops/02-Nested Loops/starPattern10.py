"""
Generating a hollow right angle triangle pattern, given the number of rows
*
* *
*   *
*     *
* * * * *
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowIndex):
        if(columnIndex == 1 or columnIndex == rowIndex or rowIndex == rowRange):
            print("*",end=" ")
        else:
            print(" ", end=" ")
            
        columnIndex += 1
    
    rowIndex += 1
    print()
    