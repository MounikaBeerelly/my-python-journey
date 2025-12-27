#!python3

import os
os.system("cls")

print(" ")
print("\nIllustration of \"Zip\" function in python")
print("--------------------OoO-------------------")

itemsinBasket = ["Scissors", "Paper Packs", "Glue Sticks", "Erasers", "Staple Pins"]
itemsPrice = [15.25, 125, 5.35, 3.25, 7.75]
itemsQuantity = [10,25, 15, 20, 5]

print("The final basket with Items , unit price and Quantity..", end="\n")

for basketItem, itemPrice, itemQuantity in zip(itemsinBasket,itemsPrice,itemsQuantity):
    print("Item %s is priced at %0.2f was Purchased with a quantity of : %d"%(basketItem,itemPrice,itemQuantity), end="\n")