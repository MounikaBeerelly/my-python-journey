import os
os.system("cls")

import functools

myPrices = [25, 9, 35, 16, 45, 28, 32, 15, 8, 26]
myQuantities = [8, 4, 5, 2, 7, 12, 11, 4, 9, 6]

print("\nThe price of the items purchased: ", list(myPrices), end="\n")
print("\nThe quantity purchased for each item is: ", list(myQuantities), end="\n")

print("\nCalculating the final cost of the items along with their quantity purchased.....", end="")

finalCost = functools.reduce(lambda priceValue01, quantityValue01 : priceValue01 + quantityValue01, [inPrice * inQuantity for inPrice, inQuantity in zip(myPrices, myQuantities)])

print("\nThe reference to the final cost is: ", finalCost, end="\n")

"""
Output:
-------
The price of the items purchased:  [25, 9, 35, 16, 45, 28, 32, 15, 8, 26]

The quantity purchased for each item is:  [8, 4, 5, 2, 7, 12, 11, 4, 9, 6]

Calculating the final cost of the items along with their quantity purchased.....
The reference to the final cost is:  1734
"""
