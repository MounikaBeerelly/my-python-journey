"""
Scenario: Printing a square number pattern of 1's
1 1 1
1 1 1
1 1 1
"""

#!python3 

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the row range value:"))

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowRange):
        print("1", end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()