#!python3

import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball", "Swimming", "Volley Ball"]

print("\nThe Original identified Sports are: ", listOfSports, end="\n")
 
del listOfSports[1 : 3] 
print("\nThe final list after slicing for deletion is: ", list(listOfSports), end="\n")        

del listOfSports[2 :  4]
print("\nThe final list after slicing for deletion is: ", list(listOfSports), end="\n")        

"""
Output:
-------
The Original identified Sports are:  ['Cricket', 'football', 'Shuttle', 'Base Ball', 'Swimming', 'Volley Ball']

The final list after slicing for deletion is:  ['Cricket', 'Base Ball', 'Swimming', 'Volley Ball']

The final list after slicing for deletion is:  ['Cricket', 'Base Ball']
"""