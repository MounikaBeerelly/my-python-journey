"""
Scenario: Printing a square number pattern of 1's and 0's at odd even positions. Starting with 1's and alternatively with 0's
0 1 0 
0 1 0
0 1 0
"""

#!python3 

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the row range value:"))
columnRange = int(input("Please enter the number of columns to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= columnRange):
        print("%d"%(not(columnIndex%2)), end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()

