"""
Generate number pattern like below:
1
12
123
1234
12345
"""

import os
os.system("cls")

rowRange = int(input("Please enter the number of rows to be generated:"))

rowIndex = 1

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print("%d"%(columnIndex), end=" ")
        columnIndex += 1
    
    rowIndex += 1
    print()