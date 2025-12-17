#!python3

import os
os.system("cls")

import calendar

inMonth = int(input("\nPlease enter the required month : "))
inYear = int(input("\nPlease enter the required year : "))

print(f"\nThe calendar for the month {inMonth} of year {inYear} is...", end = "\n")

print(calendar.month(inYear, inMonth, 4, 3))

"""
Output:
-------

Please enter the required month : 2

Please enter the required year : 2024

The calendar for the month 2 of year 2024 is...
          February 2024


Mon  Tue  Wed  Thu  Fri  Sat  Sun


                 1    2    3    4


  5    6    7    8    9   10   11


 12   13   14   15   16   17   18


 19   20   21   22   23   24   25


 26   27   28   29

"""