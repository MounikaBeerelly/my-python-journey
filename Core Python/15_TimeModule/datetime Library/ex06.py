#!python3

import os
os.system("cls")

from datetime import date

todaysDate = date.today()

print("\nThe returned date is : ", todaysDate, end = "\n")
print("\nThe Current Year is : ", todaysDate.year, end = "\n")
print("\nThe Current Month is : ", todaysDate.month, end = "\n")
print("\nThe Current Day is : ", todaysDate.day, end = "\n")


"""
Output:
-------
The returned date is :  2025-12-17

The Current Year is :  2025

The Current Month is :  12

The Current Day is :  17
"""