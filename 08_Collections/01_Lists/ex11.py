#!python3

import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball"]

print("\nPrinting the total elements in the list", end="\n")
loopCounter = 0
while loopCounter < len(listOfSports) :
    print("\nThe element in the list index", loopCounter, "is: ", listOfSports[loopCounter], end="\n")
    loopCounter += 1

myPrompt = "\nPlease enter your choice (1 to " + str(len(listOfSports)) + "): ";
# Searching the elemnt from the list using index number
inIndexNumber = int(input("\nGive th eindex to search: "))
print("\nThe sport name found is: ", listOfSports[inIndexNumber], end="\n")
"""
Output:
-------
Printing the total elements in the list

The element in the list index 0 is:  Cricket

The element in the list index 1 is:  football

The element in the list index 2 is:  Shuttle

The element in the list index 3 is:  Base Ball

Give th eindex to search: 3

The sport name found is:  Base Ball

"""