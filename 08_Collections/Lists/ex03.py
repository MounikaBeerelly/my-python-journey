#!python3

import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball"]
print("\nThe Original Identified Sports are: ", listOfSports, end="\n")

print("\nUpdating the \"Shuttle\" sport...", end="\n")

listOfSports[2] = 'Swimming'
print("\nThe Updated Sports list is: ", list(listOfSports), end="\n")
        
"""
Output:
-------
The Original Identified Sports are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

Updating the "Shuttle" sport...

The Updated Sports list is:  ['Cricket', 'football', 'Swimming', 'Base Ball']
"""