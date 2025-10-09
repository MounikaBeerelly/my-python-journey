#!python3

"""
Write a program to generate a square or rectangle Rhombus pattern
  * * *
    * * *
      * * *
"""

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Enter the number of rows to be generated:"))
columnRange = int(input("\nEnter the number of columns to be generated:"))

if(rowRange == columnRange):
    print("\nThe Rhombus Pattern generated..",end="\n")

    print()
    
    while(rowIndex <= rowRange):
        columnIndex = 1
        while(columnIndex <= rowIndex):
            print(" ", end=" ")
            columnIndex += 1
            
        columnIndex = 1
        
        while(columnIndex <= columnRange):
            print("*", end=" ")
            columnIndex += 1
            
        rowIndex += 1
        print()
        
else:
    print("\nsorry! the pattern parameters should be same values", end="\n")