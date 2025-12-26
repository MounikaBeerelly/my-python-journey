#!python3

import os
from tabulate import tabulate

os.system("cls")

def shoppingCart(inCartName, *args) :
    outTable = [[itemIndex + 1, itemName] for itemIndex, itemName in enumerate(args)]
    print(f"\nDisplaying the details of {inCartName}...",end="\n")
    print(tabulate(outTable, headers = ["Item #", "Item Name"], tablefmt = "pretty"))
        
print("\nIllustration of Variable Argument function")
print("--------------------------------------------", end="\n")

print("\nCalling the variable argument function to carry the information of shoppig cart...", end="\n")

shoppingCart("Shopping Cart 01", "Bananas", "Apples", "Oranges", "Grapes", "Pressimons")

shoppingCart("Shopping Cart 02", "Pencils", "Erasers", "Books", "Scale")

shoppingCart("Shopping Cart 03", "Buscuits", "Chips", "Chocolates")

"""
Output:
=======

Illustration of Variable Argument function
--------------------------------------------

Calling the variable argument function to carry the information of shoppig cart...

Displaying the details of Shopping Cart 01...
+--------+------------+
| Item # | Item Name  |
+--------+------------+
|   1    |  Bananas   |
|   2    |   Apples   |
|   3    |  Oranges   |
|   4    |   Grapes   |
|   5    | Pressimons |
+--------+------------+

Displaying the details of Shopping Cart 02...
+--------+-----------+
| Item # | Item Name |
+--------+-----------+
|   1    |  Pencils  |
|   2    |  Erasers  |
|   3    |   Books   |
|   4    |   Scale   |
+--------+-----------+

Displaying the details of Shopping Cart 03...
+--------+------------+
| Item # | Item Name  |
+--------+------------+
|   1    |  Buscuits  |
|   2    |   Chips    |
|   3    | Chocolates |
+--------+------------+
"""

