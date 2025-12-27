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
completed generating the multiplication table for 1

2 * 1 = 2
   .
   .

completed generating the multiplication table for 2

Write the logic for genereating upto 5 tables, with each table upto 5

"""

#!python3

import os
os.system("cls")

rowIndex = 1

while(rowIndex <= 5): # manages the row index
    columnIndex = 1
    print("\nNow generating the multiplication table for %2d"%(rowIndex),end="\n")
    while(columnIndex <= 10): # manages the column index
        print("%2d * %2d = %2d"%(rowIndex, columnIndex,(rowIndex * columnIndex)), end="\n")
        columnIndex += 1
    else:
        print("\nCompleted generating the multiplication table for %2d"%(rowIndex),end="\n")
        
    rowIndex += 1
    print("\n")
else:
    print("\ncompleted generating all the multiplication tables...",end="\n")