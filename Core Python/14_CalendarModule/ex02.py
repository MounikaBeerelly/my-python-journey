#!python3

import os
os.system("cls")

import calendar

inMonth = int(input("\nPlease enter the required month : "))
inYear = int(input("\nPlease enter the required year : "))

print(f"\nThe calendar for the month {inMonth} of year {inYear} is...", end = "\n")

print(calendar.month(inYear, inMonth))

"""
Output:
-------
Please enter the required month : 12

Please enter the required year : 2025

The calendar for the month 12 of year 2025 is...
   December 2025
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

"""