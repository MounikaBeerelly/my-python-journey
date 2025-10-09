"""
Scenario:
=========
Write a program to generate multiplication table representing in the following format

Sample Output:
==============
1 * 1 = 1
1 * 2 = 2
   .
   .
   .
2 * 1 = 2
   .
   .
Write the logic for genereating upto 5 tables, with each table upto 5

"""

#!python3

import os
os.system("cls")

rowIndex = 1

while(rowIndex <= 5): # manages the row index
    columnIndex = 1
    while(columnIndex <= 5): # manages the column index
        print("%2d * %2d = %2d"%(rowIndex, columnIndex,(rowIndex * columnIndex)), end="\n")
        columnIndex += 1
        
    rowIndex += 1
    print("\n")