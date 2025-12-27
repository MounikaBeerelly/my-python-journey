"""
Scenario:
---------
Generate a pattern of 0's and 1's simulating the chessboard positions
    1. 0: representing black
    2. 1: representing white
------------
10101010
01010101
10101010
01010101
10101010
01010101
10101010
01010101
"""

#!python3

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))
columnRange = int(input("Please enter the number of columns to be generated:"))

boxCondition = 1

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= columnRange):
        if(boxCondition == 1):
            print("1", end=" ")
        else:
            print("0",end=" ")
            
        columnIndex += 1
        boxCondition *= -1
    
    if(columnRange % 2 == 0):
        boxCondition *= -1
    
    rowIndex += 1
    print()