#!python3

import os
os.system("cls")

# Defining the List
listOfSports01 = ["Cricket", "football", "Shuttle", "Base Ball"]
listOfSports02 = ["Swimming", "Kabaddi", "Volley Ball", "football"]

print("\nThe Original identified Sports in List 01 are: ", list(listOfSports01), end="\n")
print("\nThe Original identified Sports in List 02 are: ", list(listOfSports02), end="\n")

# Merging the lists
finalList = listOfSports01 + listOfSports02
 
print("\nThe total length of the final list is : ", len(finalList), end="\n")
print("\nPrinting the total elements in the list after merging all the elements", end="\n")
loopCounter = 0
while loopCounter < len(finalList) :
    print("\nThe element in final list index", loopCounter, "is: ", finalList[loopCounter], end="\n")
    loopCounter += 1

#Counting
readElement = input("\nPlease give the element to count: ")
print("\nThe element given for counting is: ", readElement, end="\n")
print("\nThe element is found : ", finalList.count(readElement), "Time(s)", end = "\n")

"""
Output:
-------

The Original identified Sports in List 01 are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

The Original identified Sports in List 02 are:  ['Swimming', 'Kabaddi', 'Volley Ball', 'football']

The total length of the final list is :  8

Printing the total elements in the list after merging all the elements

The element in final list index 0 is:  Cricket

The element in final list index 1 is:  football

The element in final list index 2 is:  Shuttle

The element in final list index 3 is:  Base Ball

The element in final list index 4 is:  Swimming

The element in final list index 5 is:  Kabaddi

The element in final list index 6 is:  Volley Ball

The element in final list index 7 is:  football

Please give the element to count: football

The element given for counting is:  football

The element is found :  2 Time(s)
"""