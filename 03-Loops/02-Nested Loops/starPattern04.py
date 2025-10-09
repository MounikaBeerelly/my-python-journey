#!python3

"""
Write a program to generate hollow square orr rectangle pattern
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Enter the number of rows to be generated:"))
columnRange = int(input("\nEnter the number of columns to be generated:"))

if(rowRange == columnRange):
    print("\nThe Pattern generated is a square..",end="\n")

if(rowRange > columnRange):
    print("\nThe Pattern generated is a vertical rectangle..",end="\n")
     
if(rowRange < columnRange):
    print("\nThe Pattern generated is a horizontal rectangle..",end="\n")
  
print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= columnRange):
        if(rowIndex == 1 or rowIndex == rowRange or columnIndex == 1 or columnIndex == columnRange):
            print("*",end=" ")
        else:
            print(" ", end=" ")
        
        columnIndex += 1
    
    rowIndex += 1
    print()
     