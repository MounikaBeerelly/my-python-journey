#!python3

import os
os.system("cls")

from calendar import Calendar

inMonth = int(input("\nPlease enter the required month : "))
inYear = int(input("\nPlease enter the required year : "))

print("\nPrinting the Calendar with Month dates", end="\n")
    
calendarObject = Calendar()

for indexDay in calendarObject.itermonthdays2(inYear, inMonth) :
    print("\nThe current day is : ",indexDay, end="\n")  

"""
Output:
-------

Please enter the required month : 1

Please enter the required year : 2024

Printing the Calendar with Month dates

The current day is :  (1, 0)

The current day is :  (2, 1)

The current day is :  (3, 2)

The current day is :  (4, 3)

The current day is :  (5, 4)

The current day is :  (6, 5)

The current day is :  (7, 6)

The current day is :  (8, 0)

The current day is :  (9, 1)

The current day is :  (10, 2)

The current day is :  (11, 3)

The current day is :  (12, 4)

The current day is :  (13, 5)

The current day is :  (14, 6)

The current day is :  (15, 0)

The current day is :  (16, 1)

The current day is :  (17, 2)

The current day is :  (18, 3)

The current day is :  (19, 4)

The current day is :  (20, 5)

The current day is :  (21, 6)

The current day is :  (22, 0)

The current day is :  (23, 1)

The current day is :  (24, 2)

The current day is :  (25, 3)

The current day is :  (26, 4)

The current day is :  (27, 5)

The current day is :  (28, 6)

The current day is :  (29, 0)

The current day is :  (30, 1)

The current day is :  (31, 2)

The current day is :  (0, 3)

The current day is :  (0, 4)

The current day is :  (0, 5)

The current day is :  (0, 6)

"""