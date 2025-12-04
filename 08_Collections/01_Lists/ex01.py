#!python3

import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball"]

print("\nDifferent sports registered in the system are: ", listOfSports, end="\n")
print("\nDifferent sports registered in the system are: ", list(listOfSports), end="\n")

#Indexing
print("\n---------------Printing the List with Positive Indexing: Forward Traversal-------------------", end="\n")
print("\nIn Sports List Index 0 is: ", listOfSports[0], end="\n")
print("\nIn Sports List Index 1 is: ", listOfSports[1], end="\n")
print("\nIn Sports List Index 2 is: ", listOfSports[2], end="\n")
print("\nIn Sports List Index 3 is: ", listOfSports[3], end="\n")

print("\n---------------Printing the List with Negative Indexing: Backward Traversal-------------------", end="\n")
print("\nIn Sports List Index 3 is: ", listOfSports[-1], end="\n")
print("\nIn Sports List Index 2 is: ", listOfSports[-2], end="\n")
print("\nIn Sports List Index 1 is: ", listOfSports[-3], end="\n")
print("\nIn Sports List Index 0 is: ", listOfSports[-4], end="\n")

# Slicing
listOfValues = [23, 56, 12, 87, 34, 9, 65, 10]

print("\n---------------Understanding Slicing Concept------------------", end="\n")
print("\nSlicing for all the values: ", listOfValues[:], end="\n")

print("\nPresenting the data from first Index to last element: ", listOfValues[0 :], end="\n")
print("\nPresenting the data from second Index to last element: ", listOfValues[1 :], end="\n")
print("\nPresenting the data from first Index to fifth element: ", listOfValues[: 5], end="\n")
print("\nPresenting the data from third Index to seventh element: ", listOfValues[2 : 7], end="\n")

print("\nPresenting the data from forth Index upto 4 elements from the index position: ", listOfValues[4 : 8], end="\n")


"""
Output:
-------

Different sports registered in the system are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

Different sports registered in the system are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

---------------Printing the List with Positive Indexing: Forward Traversal-------------------

In Sports List Index 0 is:  Cricket

In Sports List Index 1 is:  football

In Sports List Index 2 is:  Shuttle

In Sports List Index 3 is:  Base Ball

---------------Printing the List with Negative Indexing: Backward Traversal-------------------

In Sports List Index 3 is:  Base Ball

In Sports List Index 2 is:  Shuttle

In Sports List Index 1 is:  football

In Sports List Index 0 is:  Cricket

---------------Understanding Slicing Concept------------------

Slicing for all the values:  [23, 56, 12, 87, 34, 9, 65, 10]

Presenting the data from first Index to last element:  [23, 56, 12, 87, 34, 9, 65, 10]

Presenting the data from second Index to last element:  [56, 12, 87, 34, 9, 65, 10]

Presenting the data from first Index to fifth element:  [23, 56, 12, 87, 34]

Presenting the data from third Index to seventh element:  [12, 87, 34, 9, 65]

Presenting the data from forth Index upto 4 elements from the index position:  [34, 9, 65, 10]
"""