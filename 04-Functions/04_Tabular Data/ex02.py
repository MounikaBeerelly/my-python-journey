#!python3

import os
from tabulate import tabulate

os.system("cls")

def shoppingCart(inCartName, *args) :
    outTable = [[itemIndex + 1, itemPrice] for itemIndex, itemPrice in enumerate(args)]
    print(f"\nDisplaying the details of {inCartName}...",end="\n")
    print(tabulate(outTable, headers = ["Item #", "Item Price"], tablefmt = "pretty", stralign="right"))
        
print("\nIllustration of Variable Argument function")
print("--------------------------------------------", end="\n")

print("\nCalling the variable argument function to carry the information of shoppig cart prices...", end="\n")

shoppingCart("Cart 01 Prices", 23, 31.25, 46, 15.74, 62.25, 35, 75)
shoppingCart("Cart 02 Prices", 5.65, 33.65, 72, 45)
shoppingCart("Cart 03 Prices", 5, 45, 37, 28, 75, 56.45)

"""
Output:
=======

Illustration of Variable Argument function
--------------------------------------------

Calling the variable argument function to carry the information of shoppig cart prices...

Displaying the details of Cart 01 Prices...
+--------+------------+
| Item # | Item Price |
+--------+------------+
|      1 |         23 |
|      2 |      31.25 |
|      3 |         46 |
|      4 |      15.74 |
|      5 |      62.25 |
|      6 |         35 |
|      7 |         75 |
+--------+------------+

Displaying the details of Cart 02 Prices...
+--------+------------+
| Item # | Item Price |
+--------+------------+
|      1 |       5.65 |
|      2 |      33.65 |
|      3 |         72 |
|      4 |         45 |
+--------+------------+

Displaying the details of Cart 03 Prices...
+--------+------------+
| Item # | Item Price |
+--------+------------+
|      1 |          5 |
|      2 |         45 |
|      3 |         37 |
|      4 |         28 |
|      5 |         75 |
|      6 |      56.45 |
+--------+------------+
"""

