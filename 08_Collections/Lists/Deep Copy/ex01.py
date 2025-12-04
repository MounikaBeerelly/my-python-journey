#!python3

import os
os.system("cls")

import copy 

listSports01 = ["Cricket", "Football", "Chess", "Shuttle"]

print("\nPrinting the elements from the source object ID : ", id(listSports01), end="\n")
print("\nThe elements in the source object list : ", list(listSports01), end="\n")

listSports02 = copy.deepcopy(listSports01)

print("\nPrinting the elements from the target object ID : ", id(listSports02), end="\n")
print("\nThe elements in the target object list : ", list(listSports02), end="\n")


"""
Output:
-------
Printing the elements from the source object ID :  1612830680832

The elements in the source object list :  ['Cricket', 'Football', 'Chess', 'Shuttle']

Printing the elements from the target object ID :  1612829364160

The elements in the target object list :  ['Cricket', 'Football', 'Chess', 'Shuttle']
"""