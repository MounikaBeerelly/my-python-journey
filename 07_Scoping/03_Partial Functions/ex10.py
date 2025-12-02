#!python3

"""
Domain : E-commerce
Scenario: Calculate price after applying different discount rates
"""

import os
os.system("cls")

from functools import partial

def calculatePrice(inPrice, inDiscount, inQuantity) :
    def calculateGrossPrice(inPrice, inQuantity) :
        return inPrice * inQuantity
    
    grossPrice = calculateGrossPrice(inPrice, inQuantity)
    return grossPrice - (grossPrice * inDiscount)

if __name__ == "__main__" :
    print("\nCalculating the final price after applying the possible discount", end="\n")
    
    discount10Percent = partial(calculatePrice, inDiscount = 0.10)
    discount20Percent = partial(calculatePrice, inDiscount = 0.20)

    inPrice = float(input("\nPlease enter the original price of the item: "))
    inQuantity = int(input("\nEnter the quantity purchased : "))
    
    if inQuantity >= 5 and inQuantity <= 10 :
        print(f"\nThe final price of the item after 10% discount is : {discount10Percent(inPrice = inPrice, inQuantity = inQuantity)}", end="\n")
    elif inQuantity > 10 :
        print(f"\nThe final price of the item after 20% discount is : {discount20Percent(inPrice = inPrice, inQuantity = inQuantity)}", end="\n")
    else :
        print(f"\nThe final price of the item without discount is : {calculatePrice(inPrice = inPrice, inQuantity = inQuantity, inDiscount = 0)}", end="\n")

    
"""
Output:
------
Calculating the final price after applying the possible discount

Please enter the original price of the item: 250

Enter the quantity purchased : 10

The final price of the item after 10% discount is : 2250.0
"""