#!python3

import os
from tabulate import tabulate
os.system("cls")

def itemPrices(*args) :
    itemIndex = 0
    totalPrice = 0
    
    outTable =[]
    for varArgsIndex in args :
        outTable.append([itemIndex + 1, varArgsIndex, totalPrice + varArgsIndex])
        itemIndex += 1
        totalPrice += varArgsIndex
        
    print("\nDisplaying the details of the Item prices, calculates with cumulative price..", end="\n")
    print(tabulate(outTable, headers = ["Item #", "Price", "Running total"], tablefmt = "pretty", floatfmt = ".2f", stralign = "right"))
    
    return totalPrice
        
print("\nIllustration of Variable Argument function")
print("--------------------------------------------", end="\n")

print("\nCalling the variable argument function to carry the information of item prices...", end="\n")

finalTotalPrice = itemPrices(200, 150, 45, 190, 49)

print(f"\nThe total cost of all the items is: {finalTotalPrice : .2f}", end="\n")
print("\nFinished printing the shopping cart.. Terminating the application", end="\n")

"""
Output:
=======
Illustration of Variable Argument function
--------------------------------------------

Calling the variable argument function to carry the information of item prices...

Displaying the details of the Item prices, calculates with cumulative price..
+--------+-------+---------------+
| Item # | Price | Running total |
+--------+-------+---------------+
|      1 |   200 |           200 |
|      2 |   150 |           350 |
|      3 |    45 |           395 |
|      4 |   190 |           585 |
|      5 |    49 |           634 |
+--------+-------+---------------+

The total cost of all the items is:  634.00

Finished printing the shopping cart.. Terminating the application
"""

