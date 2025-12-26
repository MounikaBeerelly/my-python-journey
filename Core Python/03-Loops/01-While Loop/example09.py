"""
Scenario:
---------
Write a program to generate the multiplication table for any number of the table that is supplied by the end user
The table should be displayed in the below format

1 * 1 = 01
1 * 2 = 02
.
.
The table should be generated upto 10 as a count of implementation
"""

#!python3

import os
os.system("cls")

tableNumber = tableIndex = 1

tableNumber = int(input("\nPlease ener the multiplication table to be generated:"))

print("\nPrinting the multiplication table for: %d"%(tableNumber), end="\n")

while(tableIndex <= 10):
    #print("%d" %(tableNumber),"* %02d"%(tableIndex),"=%02d"%(tableNumber * tableIndex))
    print("%d * %02d = %02d" %(tableNumber,tableIndex, tableNumber * tableIndex))
    tableIndex += 1   
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")



