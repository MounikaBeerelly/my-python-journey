"""
Printing a square number pattern of alphabets
A
A B
A B C
A B C D
A B C D E
"""

import os
os.system("cls")

rowIndex = 1
AsciiCount = 0

rowRange = int(input("Please enter the number of rows to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    AsciiCount = 0
    while(columnIndex <= rowIndex):
        print(chr(65+AsciiCount), end=" ")
        columnIndex += 1
        AsciiCount += 1
    
    rowIndex += 1
    print()