"""
Generating a Inverted mirrored right angle triangle pattern, given the number of rows
  * * * * *
    * * * *
      * * *
        * *
          *
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print(" ",end=" ")
        columnIndex += 1
    
    columnIndex = rowIndex
    while(columnIndex <= rowRange):
        print("*",end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()
    