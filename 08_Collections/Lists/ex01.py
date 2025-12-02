#!python3

import os
os.system("cls")

# Define the List
stationaryItems = ["Pencils", "Eracers", "Pens", "Papers", "Exam Pads", "Glue Sticks", "Crayons", "Envelops"]

# Type of the variable
print("\nThe calss type is : ", type(stationaryItems))

# Display the data
print("\nThe Stationary items are: ", stationaryItems, end="\n")

# Show the items using indexes
print("\nFirst Stationary item is: ", stationaryItems[0], end="\n")
print("\nSecondary Stationary item is: ", stationaryItems[2], end="\n")
print("\nLast Stationary item is: ", stationaryItems[-1], end="\n")

# Length of the List
print("\nLength of the StationaryList is: ", len(stationaryItems), end="\n")

# Slicing the list
print("\nThe Range of the StationaryList items are: ", str(stationaryItems[2:6]), end="\n")
print("\nThe Range of the StationaryList items are: ", str(stationaryItems[0:3]), end="\n")

# Check the item is in the list
print("\nThe status for item \"Pencils\" is : ", str("Pencils" in stationaryItems), end="\n")
print("\nThe status for item \"pencils\" is : ", str("pencils" in stationaryItems), end="\n")

# Check the item is not in the list
print("\nThe status for item \"paper\" is : ", str("paper" not in stationaryItems), end="\n")

# Nested List
employeeInfo = [['John', 'Doe'], ['john@gmail.com', 9876543210], [52, 134.12]]
print("\nThe name of the employee is :", str(employeeInfo[0]))
print("\nThe First name of the employee is :", employeeInfo[0][0])

# Deep Nesting
employeeInfo = [['John', ['Kumar', ['Doe']]], ['john@gmail.com', [9876543210]], [[52], 134.12]]
print("\nThe lastname of the employee is :", str(employeeInfo[0][1][1]))


"""
Output:
-------

The calss type is :  <class 'list'>

The Stationary items are:  ['Pencils', 'Eracers', 'Pens', 'Papers', 'Exam Pads', 'Glue Sticks', 'Crayons', 'Envelops']

First Stationary item is:  Pencils

Secondary Stationary item is:  Pens

Last Stationary item is:  Envelops

Length of the StationaryList is:  8

The Range of the StationaryList items are:  ['Pens', 'Papers', 'Exam Pads', 'Glue Sticks']

The Range of the StationaryList items are:  ['Pencils', 'Eracers', 'Pens']

The status for item "Pencils" is :  True

The status for item "pencils" is :  False

The status for item "paper" is :  True

The name of the employee is : ['John', 'Doe']

The First name of the employee is : John

The lastname of the employee is : ['Doe']
"""