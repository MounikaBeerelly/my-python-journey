#!python3

import os
os.system("cls")

import time

myActualTime = time.localtime(time.time())

print("\nThe local time is : ", myActualTime, end="\n")

print("\nThe Current Year is : ", myActualTime.tm_year, end="\n")
print("\nThe Current Month is : ", myActualTime.tm_mon, end="\n")
print("\nThe Current Month day is : ", myActualTime.tm_mday, end="\n")


"""
Output:
-------
The local time is :  time.struct_time(tm_year=2025, tm_mon=12, tm_mday=17, tm_hour=10, tm_min=54, tm_sec=8, tm_wday=2, tm_yday=351, tm_isdst=0)

The Current Year is :  2025

The Current Month is :  12

The Current Month day is :  17
"""