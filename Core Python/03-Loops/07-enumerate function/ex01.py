#!python3

import os
os.system("cls")

print(" ")
print("\nIllustration of \"enumerate\" function in python")
print("--------------------OoO-------------------")

itemsinBasket = ["Scissors", "Paper Packs", "Glue Sticks", "Erasers", "Staple Pins"]

print("\nEnumerating the items in the basket..", end="\n")

enumeratingObject = enumerate(itemsinBasket, start=1)

for extractedItem in enumeratingObject:
    print(extractedItem)