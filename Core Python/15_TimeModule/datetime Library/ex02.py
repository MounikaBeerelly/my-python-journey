#!python3

import os
os.system("cls")

import datetime 

currentDate = datetime.datetime.now()

print("\nThe Current date is : ", currentDate, end = "\n")

print("\nThe Current Year is : ", currentDate.strftime("%y"),",",currentDate.strftime("%Y"), end="\n")
print("\nThe Current Month is : ", currentDate.strftime("%m"),",",currentDate.strftime("%B"),",",currentDate.strftime("%b"), end="\n")
print("\nThe Current Week Day is : ", currentDate.strftime("%w"),",",currentDate.strftime("%A"),",",currentDate.strftime("%a"), end="\n")
print("\nThe Current Hour in 12 Hour Clock Mode is : ", currentDate.strftime("%I"),",",currentDate.strftime("%p"), end="\n")
print("\nThe Current Hour in 24 Hour Clock Mode is : ", currentDate.strftime("%H"), end="\n")
print("\nThe Current Time is : ", currentDate.strftime("%H"),",",currentDate.strftime("%M"),",",currentDate.strftime("%S"), end="\n")
print("\nThe Micro Seconds is : ", currentDate.strftime("%f"), end="\n")
print("\nThe TimeZone is : ", currentDate.strftime("%Z"), end="\n")
print("\nThe Julian Day is : ", currentDate.strftime("%j"), end="\n")
print("\nThe Year week number with Sunday as the First day is : ", currentDate.strftime("%U"), end="\n")
print("\nThe Year week number with Monday as the First day is : ", currentDate.strftime("%W"), end="\n")
print("\nThe Date and Time in Local version is : ", currentDate.strftime("%c"), end="\n")


"""
Output:
-------

The Current date is :  2025-12-17 12:13:44.341289

The Current Year is :  25 , 2025

The Current Month is :  12 , December , Dec

The Current Week Day is :  3 , Wednesday , Wed

The Current Hour in 12 Hour Clock Mode is :  12 , PM

The Current Hour in 24 Hour Clock Mode is :  12

The Current Time is :  12 , 13 , 44

The Micro Seconds is :  341289

The TimeZone is :

The Julian Day is :  351

The Year week number with Sunday as the First day is :  50

The Year week number with Monday as the First day is :  50

The Date and Time in Local version is :  Wed Dec 17 12:13:44 2025
"""