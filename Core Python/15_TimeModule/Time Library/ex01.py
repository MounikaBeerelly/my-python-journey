#!python3

import os
os.system("cls")

import time

pythonTicks = time.time()

print("\nThe total number of ticks since January 1st, 1970, 12:00AM : ", pythonTicks, end = "\n")


"""
Output:
-------
The total number of ticks since January 1st, 1970, 12:00AM :  1765989414.681418
"""

"""
Note:
-----
1. In the context of programming and computing, ticks refer to the smallest unit of time measurement used by a system's clock
2. time.time() function returns the number of seconds (as floating-point numbers) that have elapsed since the Unix epoch
3. Ticks are useful for measuring elapsed time, scheduling tasks, or logging time-related data in a precise format
"""
    