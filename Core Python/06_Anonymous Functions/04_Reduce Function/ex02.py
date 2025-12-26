import os
os.system("cls")

import functools

myPriceList = [25, 9, 35, 16, 45, 28, 32, 15, 8, 26]

print("\nThe registered prices in the Price list are:", end="\n")

print("\nThe sum of the total prices from the price list is:", end="")
print()

cumPricelist = functools.reduce(lambda extractedPriceValue01, extractedPriceValue02 : extractedPriceValue01 + extractedPriceValue02, myPriceList)
print(cumPricelist, end="\n")

"""
Output:
-------
The registered prices in the Price list are:

The sum of the total prices from the price list is:
239
"""
