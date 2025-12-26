#!python3

import os
os.system("cls")

# Defining the List
listOfSports01 = ["Cricket", "football", "Shuttle", "Base Ball"]
listOfSports02 = ["Swimming", "Kabaddi", "Volley Ball"]

print("\nThe Original identified Sports in List 01 are: ", list(listOfSports01), end="\n")
print("\nThe Original identified Sports in List 02 are: ", list(listOfSports02), end="\n")

# Merging the lists
print("\nThe total list of sports are: ", (listOfSports01 + listOfSports02), end="\n")

"""
Output:
-------
The Original identified Sports in List 01 are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

The Original identified Sports in List 02 are:  ['Swimming', 'Kabaddi', 'Volley Ball']

The total list of sports are:  ['Cricket', 'football', 'Shuttle', 'Base Ball', 'Swimming', 'Kabaddi', 'Volley Ball']
"""