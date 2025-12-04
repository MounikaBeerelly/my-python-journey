#!python3

import os
os.system("cls")

stationaryItemsSet01 = {"Pencils", "Papers", "Erasers", "Pens"}
print("\nList of elements in first Set : ",set(stationaryItemsSet01))

stationaryItemsSet02 = {"Glue Sticks", "Erasers", "Exam Pads", "Pencils"}
print("\nList of elements in second Set : ",set(stationaryItemsSet02))

# Intersection
intersectionStationary = stationaryItemsSet01.intersection(stationaryItemsSet02)

print("\nThe Intersection of two stationaries are: ", set(intersectionStationary), end="\n")

# Intersection_update
stationaryItemsSet01.intersection_update(stationaryItemsSet02)

print("\nThe Intersection update of two stationaries are: ", set(stationaryItemsSet01), end="\n")

"""
Output:
-------
List of elements in first Set :  {'Erasers', 'Pens', 'Papers', 'Pencils'}

List of elements in second Set :  {'Erasers', 'Exam Pads', 'Pencils', 'Glue Sticks'}

The Intersection of two stationaries are:  {'Erasers', 'Pencils'}

The Intersection update of two stationaries are:  {'Erasers', 'Pencils'}
"""