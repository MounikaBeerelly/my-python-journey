#!python3

import os
os.system("cls")

def shoppingCart(*args) :
    for varArgsIndex, cartValue in enumerate(args, start =1) :
        print("\n%d. %s" %(varArgsIndex, cartValue), end="\n")
        
print("\nIllustration of Variable Argument function")
print("--------------------------------------------", end="\n")

print("\nCalling the variable argument function to carry the information of shoppig cart...", end="\n")

print("\nDisplaying the details of the shopping Cart 01..", end="\n")
shoppingCart("Bananas", "Apples", "Oranges", "Grapes", "Pressimons")

print("\nDisplaying the details of the shopping Cart 02..", end="\n")
shoppingCart("Pencils", "Erasers", "Books", "Scale")

print("\nDisplaying the details of the shopping Cart 03..", end="\n")
shoppingCart("Buscuits", "Chips", "Chocolates")

"""
Output:
=======

Illustration of Variable Argument function
--------------------------------------------

Calling the variable argument function to carry the information of shoppig cart...

Displaying the details of the shopping Cart 01..

1. Bananas

2. Apples

3. Oranges

4. Grapes

5. Pressimons

Displaying the details of the shopping Cart 02..

1. Pencils

2. Erasers

3. Books

4. Scale

Displaying the details of the shopping Cart 03..

1. Buscuits

2. Chips

3. Chocolates
"""

