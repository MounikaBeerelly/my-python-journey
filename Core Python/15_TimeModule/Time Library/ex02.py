#!python3

import os
os.system("cls")

import time

pythonTicks = time.time()

myLocalTime = time.localtime(pythonTicks)

print("\nThe returned Local Time is : ", myLocalTime, end="\n")

"""
Output:
-------
The returned Local Time is :  
time.struct_time(
    tm_year=2025, 
    tm_mon=12, 
    tm_mday=17, 
    tm_hour=10, 
    tm_min=43, 
    tm_sec=42, 
    tm_wday=2, 
    tm_yday=351, 
    tm_isdst=0
)
"""
