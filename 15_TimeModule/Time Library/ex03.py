#!python3

import os
os.system("cls")

import time

pythonTicks = time.time()

myLocalTime = time.localtime(pythonTicks)

myAscLocalTime = time.asctime(myLocalTime)
print("\nThe returned ASC Time is : ", myAscLocalTime, end="\n")

myLocalCTime = time.ctime(pythonTicks)
print("\nThe returned Local time in string format is : ", myLocalCTime, end="\n")

"""
Output:
-------
The returned ASC Time is :  Wed Dec 17 10:50:00 2025

The returned Local time in string format is :  Wed Dec 17 10:50:00 2025
"""
