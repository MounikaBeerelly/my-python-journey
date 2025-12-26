#!python3

import os
os.system("cls")

# Defining the List
listOfSports01 = ["Cricket", "Football", "Shuttle", "Base Ball"]
listOfSports02 = ["Swimming", "Kabaddi", "Volley Ball"]

print("\nThe Original identified Sports in List 01 are: ", list(listOfSports01), end="\n")
print("\nThe Original identified Sports in List 02 are: ", list(listOfSports02), end="\n")

# Merging the lists
listOfSports01.extend(listOfSports02)

print("\nPrinting the total elements in the final list", list(listOfSports01), end="\n") 

# index of the element
print("\nThe index allocated for sport \"Foot ball\" is :", listOfSports01.index("Football"), end="\n")

# insert the element 
listOfSports01.insert(2, "Chess")
print("\nPrinting the total elements in the list: ", list(listOfSports01), end="\n")

# Reverse the list
listOfSports01.reverse()
print("\nPrinting the total elements in the list after reverse: ", list(listOfSports01), end="\n")

# Sorting the list - ascending order
listOfSports01.sort()
print("\nPrinting the total elements in the list after sorting: ", list(listOfSports01), end="\n")

# Sorting the list - descending order
listOfSports01.sort(reverse = True)
print("\nPrinting the total elements in the list after sorting: ", list(listOfSports01), end="\n")

"""
Output:
-------

The Original identified Sports in List 01 are:  ['Cricket', 'Football', 'Shuttle', 'Base Ball']

The Original identified Sports in List 02 are:  ['Swimming', 'Kabaddi', 'Volley Ball']

Printing the total elements in the final list ['Cricket', 'Football', 'Shuttle', 'Base Ball', 'Swimming', 'Kabaddi', 'Volley Ball']

The index allocated for sport "Foot ball" is : 1

Printing the total elements in the list:  ['Cricket', 'Football', 'Chess', 'Shuttle', 'Base Ball', 'Swimming', 'Kabaddi', 'Volley Ball']

Printing the total elements in the list after reverse:  ['Volley Ball', 'Kabaddi', 'Swimming', 'Base Ball', 'Shuttle', 'Chess', 'Football', 'Cricket']

Printing the total elements in the list after sorting:  ['Base Ball', 'Chess', 'Cricket', 'Football', 'Kabaddi', 'Shuttle', 'Swimming', 'Volley Ball']

Printing the total elements in the list after sorting:  ['Volley Ball', 'Swimming', 'Shuttle', 'Kabaddi', 'Football', 'Cricket', 'Chess', 'Base Ball']
"""