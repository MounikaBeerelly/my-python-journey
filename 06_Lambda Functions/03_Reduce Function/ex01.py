import os
os.system("cls")

myPriceList = [25, 9, 35, 16, 45, 28, 32, 15, 8, 26]

print("\nThe registered prices in the Price list are:", end="\n")

print("\nThe sum of the total prices from the price list is:", end="")
print()
# -----------Using loops-------------

cumPriceList = 0
for extractedPrice in myPriceList :
    cumPriceList += extractedPrice

print("\nUsing loop - ", cumPriceList, end="\n")

# --------Using function---------------
def getTotalPrice(inPriceList) :
    cumPriceList = 0
    for extractedPrice in inPriceList :
        cumPriceList += extractedPrice
    return cumPriceList

cumPricelist = getTotalPrice(myPriceList)

print("\nUsing function - ", cumPricelist, end="\n")

#Using Lambda Function
cumPricelist = (lambda inPrice : getTotalPrice(inPrice))(myPriceList)
print("\nUsing Lambda function - ", cumPricelist, end="\n")

"""
Output:
-------
The registered prices in the Price list are:

The sum of the total prices from the price list is:

Using loop -  239

Using function -  239

Using Lambda function -  239
"""

"""
Note:
======
1. cumPriceList = (lambda inPrice : getTotalPrice(inPrice))(myPriceList), here (myPriceList) acts as an argument to the "lambda function".
2. "Lambda function" reads each element from the given list and passes the element as an argument to the Lambda function, which in-terms becomes as an argument to the "getTotalPrice(inPrice)" function
"""