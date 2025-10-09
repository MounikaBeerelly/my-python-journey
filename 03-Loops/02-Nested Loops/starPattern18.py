"""
Generating a flip Pyramid pattern representing the right pascals triangle arrangment OR called the right pointing half diamond.given the number of rows
*
* *
* * *
* * * *
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

columnTracker = 1

print()

while(rowIndex <= rowRange * 2):
    columnIndex = 1
    while(columnIndex <= columnTracker):
        print("*", end=" ")
        columnIndex += 1
    
    if(rowIndex < rowRange):
        columnTracker += 1
    else:
        columnTracker -= 1
        
    rowIndex += 1
    print()
    