"""
Scenario:
----------
1. Design the operational logic for a calculating the total cost of an that is purchased, with acceptable discount of 10% on the purchase only when the purchased quantity is more than OR equal to 10
"""

#!python3

import os
os.system("cls")

itemName = input("\nPlease enter the name of the item to be purchased: ")
itemPrice = float(input("\nPlease enter the price of the item: "))
itemQuantity = int(input("\nPlease enter the quantity being purchased:"))

totalCost = itemPrice * itemQuantity
finalDiscountedAmount = 0

if itemQuantity >= 10 :
    discountValue = 0.1
    finalDiscountedAmount = totalCost * discountValue
    totalCost -= finalDiscountedAmount
    print("\nHey Congratulations.. You are eligible for 10% of discount on the total bill",end="\n")
    print("\nThe disccounted amount is: %0.2f"%(finalDiscountedAmount),end="\n")

print("\nThe total cost of", itemName, "Purchased with quantity of:", itemQuantity,"with actual cost as:",(totalCost + finalDiscountedAmount),"After discount final cost is:",totalCost,end="\n")
    