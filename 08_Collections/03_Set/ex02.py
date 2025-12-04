#!python3

import os
os.system("cls")

stationaryItems = {"Pencils", "Papers", "Erasers", "Pens", "Glue Sticks", "Erasers", "Exam Pads", "Pencils"}

print("\nList of elements in Set : ",set(stationaryItems))

print("\nLength of elements in Set : ",len(stationaryItems))

stationaryItems.add("Scales")
print("\nFinal set is : ",set(stationaryItems))

"""
Output:
-------

List of elements in Set :  {'Pencils', 'Pens', 'Papers', 'Erasers', 'Glue Sticks', 'Exam Pads'}

Length of elements in Set :  6

Final set is :  {'Pencils', 'Pens', 'Scales', 'Papers', 'Erasers', 'Glue Sticks', 'Exam Pads'}

"""