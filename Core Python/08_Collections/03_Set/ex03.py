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

# Union
unionStationary = stationaryItemsSet01.union(stationaryItemsSet02)

print("\nThe Union of two stationaries are: ", set(unionStationary), end="\n")

# Difference
differenceStationary = stationaryItemsSet01.difference(stationaryItemsSet02)

print("\nThe Difference of two stationaries are: ", set(differenceStationary), end="\n")

"""
Output:
-------
List of elements in first Set :  {'Papers', 'Erasers', 'Pens', 'Pencils'}

List of elements in second Set :  {'Glue Sticks', 'Erasers', 'Exam Pads', 'Pencils'}

The Intersection of two stationaries are:  {'Erasers', 'Pencils'}

The Union of two stationaries are:  {'Pencils', 'Glue Sticks', 'Papers', 'Erasers', 'Pens', 'Exam Pads'}

The Difference of two stationaries are:  {'Pens', 'Papers'}
"""