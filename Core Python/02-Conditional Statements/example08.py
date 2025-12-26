"""
Scenario:
---------
1. Given a four digit number at runtime, confirm whether it is a leap year OR not, as a single liner logic
"""

#!python3

import os
os.system("cls")

inYear = int(input("\nPlease enter the year in 4 digits for leap year test: "))
print("\nThe given year for leap year test is: ",inYear,end="\n")

leapYearTest = "Leap Year" if(inYear %4 == 0 and inYear % 100 != 0) or (inYear%400 == 0 ) else "Not a leap year"
print("\nThe given year",inYear,"is: ",leapYearTest,end="\n")