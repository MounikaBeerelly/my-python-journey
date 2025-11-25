import os
os.system("cls")

myPrices = [24, 65, 34, 81, 56]
myTaxes = [2, 6, 3, 8, 5]

print("\nThe original price values are: ", list(myPrices), end="\n")
print("\nThe applied taxes by price values are: ", list(myTaxes), end="\n")

finalCost = map(lambda extractedPriceValue, extractedTaxValue : extractedPriceValue + extractedTaxValue, myPrices, myTaxes)

print("\nThe reference to the final cost pointed by the map function object is: ", finalCost, end="\n")

finalCostWithTaxes = list(finalCost)

print("\nThe final cost with added tax is: ", finalCostWithTaxes, end="\n")

"""
Output:
-------
The original price values are:  [24, 65, 34, 81, 56]

The applied taxes by price values are:  [2, 6, 3, 8, 5]

The reference to the final cost pointed by the map function object is:  <map object at 0x000002B127CB7E50>

The final cost with added tax is:  [26, 71, 37, 89, 61]
"""