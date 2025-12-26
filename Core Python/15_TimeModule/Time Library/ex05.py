#!python3

import os
os.system("cls")

import time

pythonTicks = time.time()

myLocalTimeStruct = time.gmtime(pythonTicks)
localTimeValue = time.mktime(myLocalTimeStruct)
localTimeStruct = time.localtime(localTimeValue)
localTimeString = time.strftime("%d-%m-%Y, %H:%M:%S", localTimeStruct)
print("\nThe returned Local time in Python Ticks is : ", localTimeString, end="\n")

"""
Output:
-------
The returned Local time in Python Ticks is :  17-12-2025, 17:45:00
"""