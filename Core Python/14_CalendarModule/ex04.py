#!python3

import os
os.system("cls")

from calendar import Calendar

print("\nPrinting the Weekday numbers that are used for one week in the Calendar", end="\n")

weekDayValues = Calendar(firstweekday = 3)

for indexWeekDay in weekDayValues.iterweekdays() :
    print("\nThe current weekday is : ", indexWeekDay, end="\n")
    

"""
Output:
-------
Printing the Weekday numbers that are used for one week in the Calendar

The current weekday is :  3

The current weekday is :  4

The current weekday is :  5

The current weekday is :  6

The current weekday is :  0

The current weekday is :  1

The current weekday is :  2
"""