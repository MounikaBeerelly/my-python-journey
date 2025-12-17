#!python3

import os
os.system("cls")

from calendar import Calendar

inMonth = int(input("\nPlease enter the required month : "))
inYear = int(input("\nPlease enter the required year : "))

print("\nPrinting the Calendar with Month dates", end="\n")
    
calendarObject = Calendar()

print("\nThe calendar object tuple is ....", end="\n")
print(calendarObject.monthdatescalendar(inYear, inMonth), end="\n")

"""
Output:
-------
Please enter the required month : 6

Please enter the required year : 2018

Printing the Calendar with Month dates

The calendar object tuple is ....
[
    [
        datetime.date(2018, 5, 28), 
        datetime.date(2018, 5, 29), 
        datetime.date(2018, 5, 30), 
        datetime.date(2018, 5, 31), 
        datetime.date(2018, 6, 1), 
        datetime.date(2018, 6, 2), 
        datetime.date(2018, 6, 3)
    ], [
        datetime.date(2018, 6, 4), 
        datetime.date(2018, 6, 5), 
        datetime.date(2018, 6, 6), 
        datetime.date(2018, 6, 7), 
        datetime.date(2018, 6, 8), 
        datetime.date(2018, 6, 9), 
        datetime.date(2018, 6, 10)
    ], [
        datetime.date(2018, 6, 11), 
        datetime.date(2018, 6, 12), 
        datetime.date(2018, 6, 13), 
        datetime.date(2018, 6, 14), 
        datetime.date(2018, 6, 15), 
        datetime.date(2018, 6, 16), 
        datetime.date(2018, 6, 17)
    ], [
        datetime.date(2018, 6, 18), 
        datetime.date(2018, 6, 19), 
        datetime.date(2018, 6, 20), 
        datetime.date(2018, 6, 21), 
        datetime.date(2018, 6, 22), 
        datetime.date(2018, 6, 23), 
        datetime.date(2018, 6, 24)
    ], [
        datetime.date(2018, 6, 25), 
        datetime.date(2018, 6, 26), 
        datetime.date(2018, 6, 27), 
        datetime.date(2018, 6, 28), 
        datetime.date(2018, 6, 29), 
        datetime.date(2018, 6, 30), 
        datetime.date(2018, 7, 1)
    ]
]
"""