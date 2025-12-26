"""
Scenario:
=========
Write a program to generate multiplication table representing a two dimensional evaluation upto 12th table
"""

#!python3

import os
os.system("cls")

rowIndex = 1

while(rowIndex <= 12): # manages the row index
    columnIndex = 1
    while(columnIndex <= 12): # manages the column index
        print("%4d"%(rowIndex * columnIndex), end="")
        columnIndex += 1
        
    rowIndex += 1
    print("\n")