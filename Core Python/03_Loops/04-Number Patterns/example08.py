"""
Scenario:
---------
Generate a pattern of *'s and .'s
------------
*.*.*.*.*.
.*.*.*.*.*
*.*.*.*.*.
.*.*.*.*.*
*.*.*.*.*.
.*.*.*.*.*
*.*.*.*.*.
.*.*.*.*.*
*.*.*.*.*.
.*.*.*.*.*
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
            print("*", end="")
        else:
            print(".",end="")
            
        columnIndex += 1
        boxCondition *= -1
    
    if(columnRange % 2 == 0):
        boxCondition *= -1
    
    rowIndex += 1
    print()