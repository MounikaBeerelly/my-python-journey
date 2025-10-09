"""
Generating a Pyramid pattern representing the pascals triangle arrangment, giiven the number of rows

            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
  * * * * * * * * * * *
* * * * * * * * * * * * *
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = rowIndex
    while(columnIndex < rowRange):
        print(" ", end=" ")
        columnIndex += 1
    
    columnIndex = 1
    while(columnIndex <= (2*rowIndex-1)):
        print("*",end=" ")
        columnIndex += 1
        
    rowIndex += 1
    print()
    