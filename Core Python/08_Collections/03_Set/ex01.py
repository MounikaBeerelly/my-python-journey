#!python3

import os
os.system("cls")

stationaryItems = {"Pencils", "Papers", "Erasers", "Pens", "Glue Sticks", "Erasers", "Exam Pads", "Pencils"}
print("\nApproach 01 : ",stationaryItems, end="\n")
print("\nApproach 02 : ",set(stationaryItems))

"""
Output:
-------
Approach 01 :  {'Erasers', 'Exam Pads', 'Papers', 'Pens', 'Glue Sticks', 'Pencils'}

Approach 02 :  {'Erasers', 'Exam Pads', 'Papers', 'Pens', 'Glue Sticks', 'Pencils'}
"""