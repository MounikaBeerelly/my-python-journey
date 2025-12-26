'''
- You have $50
- You buy an item that is $15
- With a tax of 3%
- Print how much money you have left ?
'''

import os
os.system("cls")

totalAmount = 50
itemCost = 15
tax = 0.03
remainingAmount = totalAmount - itemCost - (itemCost * tax)

print(f"Remaining amount is : {remainingAmount}")

"""
Output:
-------
Remaining amount is : 34.55
"""