"""
Generating a left flip Pyramid pattern representing the right pascals triangle arrangment OR called the right pointing half diamond.given the number of rows

          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
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

spaceManager = rowRange - 1
starManager = 1

print()

while(rowIndex <= rowRange * 2):
    columnIndex = 1
    while(columnIndex <= spaceManager):
        print(" ", end=" ")
        columnIndex += 1
    
    columnIndex = 1
    while(columnIndex <= starManager):
        print("*",end=" ")
        columnIndex += 1
        
    if(rowIndex < rowRange):
        starManager += 1
        spaceManager -= 1
    else:
        starManager -= 1
        spaceManager += 1
        
    rowIndex += 1
    print()
    