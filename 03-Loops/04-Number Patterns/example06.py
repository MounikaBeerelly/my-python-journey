"""
Scenario: Printing a square number pattern of 1's and 0's with a "0" exactly in the center of the box.
1 1 1 1 1
1 1 1 1 1
1 1 0 1 1
1 1 1 1 1
1 1 1 1 1
"""

#!python3 

import os
os.system("cls")

rowIndex = 1

rowRange = int(input("Please enter the row range value:"))
columnRange = int(input("Please enter the number of columns to be generated:"))

if(rowRange % 2) == 0:
    rowRange += 1

if(columnRange % 2) == 0:
    columnRange += 1
    
rowCenter =  (rowRange+1)/2
columnCenter = (columnRange+1)/2

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= columnRange):
        if(columnCenter == columnIndex and rowCenter == rowIndex):
            print("0", end=" ")
        else:
            if(columnRange % 2 == 0 and columnCenter+1 == columnIndex):
                if(rowCenter==rowIndex and (rowRange%2 == 0 and rowCenter+1 == rowIndex)):
                    print("0",end=" ")
                else:
                    print("1",end=" ")
            else:
                if(rowRange % 2 == 0 and rowCenter+1 == rowIndex):
                    if(columnCenter == columnIndex and (columnRange%2 == 0 and columnCenter+1 == columnIndex)):
                        print("0",end=" ")
                    else:
                        print("1",end=" ")
            print("1", end=" ")
            
        columnIndex += 1
    
    rowIndex += 1
    print()

