"""
Printing a square number pattern of alphabets
A
B C
D E F
G H I J
K L M N O
"""

import os
os.system("cls")

rowIndex = 1
AsciiCount = 0

rowRange = int(input("Please enter the number of rows to be generated:"))

print()

while(rowIndex <= rowRange):
    columnIndex = 1
    while(columnIndex <= rowIndex):
        print(chr(65+AsciiCount), end=" ")
        columnIndex += 1
        AsciiCount += 1
    
    rowIndex += 1
    print()