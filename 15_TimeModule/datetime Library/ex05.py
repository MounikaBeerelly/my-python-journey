#!python3

import os
os.system("cls")

from datetime import datetime

myDate = datetime(2024, 9, 4, 19, 47, 52)

print("\nThe given date is : ", myDate, end="\n")

date2TimeStamp = myDate.timestamp()

print("\nThe timestamp value of the given date is : ", date2TimeStamp, end = "\n")


"""
Output:
-------
The given date is :  2024-09-04 19:47:52

The timestamp value of the given date is :  1725497272.0
"""