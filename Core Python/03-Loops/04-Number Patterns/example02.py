"""
Scenario: Printing a square number pattern of 1's and 0's
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1
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
        print("%d"%(rowIndex%2), end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()

