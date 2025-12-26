#!python3

import os
os.system("cls")

print(" ")
print("\nIllustration of \"zip\" function in python")
print("------------------OoO---------------", end="\n")

itemsinBasket = ["Scissors", "Paper Packs", "Glue Sticks", "Erasers", "Staple Pins"]
itemsPrice = [15.25, 125, 5.35, 3.25, 7.75]
itemsQuantity = [10,25, 15, 20, 5]

print("\nMapping the items with quantity purchased", end="\n")

print("SNo ItemName ItemPrice Quantity TotalPrice", end="\n")

for seqId, (basketItem, itemPrice, itemQuantity) in enumerate(zip(itemsinBasket,itemsPrice,itemsQuantity),start=1):
    print("%d %s %0.2f %d %0.2f"%(seqId,basketItem,itemPrice,itemQuantity,(itemPrice*itemQuantity)), end="\n")
    
