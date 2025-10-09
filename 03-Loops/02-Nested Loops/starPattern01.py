#!python3

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the number of rows to be generated:"))

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print("*",end=" ")
        # print("%d"%(columnIndex),end=" ")
        columnIndex += 1
        
    rowIndex += 1
    print()
