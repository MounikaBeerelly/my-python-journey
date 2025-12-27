#!python3

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))
columnRange = int(input("Please enter the number of columns to be generated:"))

if(rowRange == columnRange):
    print("\nThe Pattern generated is a square..",end="\n")

if(rowRange > columnRange):
    print("\nThe Pattern generated is a vertical rectangle..",end="\n")
     
if(rowRange < columnRange):
    print("\nThe Pattern generated is a horizontal rectangle..",end="\n")
 
while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= columnRange):
        # print("*",end=" ")
        print("%d"%(columnIndex),end=" ")
        columnIndex += 1
        
    rowIndex += 1
    print()
