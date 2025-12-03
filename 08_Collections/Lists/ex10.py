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

print("\nThe Reference ID of this source list is: ", id(listOfSports), end="\n")

loopState = 1

while loopState : 
    inputState = input("\nDo you want to append new element to the list (Y OR N): ")
    
    if inputState == 'y' or inputState == 'Y' :
        appendElement = input("\nPlease enter the neew element to be appended to the list: ")
        listOfSports.append(appendElement)
        print("\nPrinting the list after appending the element: ", list(listOfSports), end="\n")
        print("\nThe Reference ID of this source list is: ", id(listOfSports), end="\n")
    else:
        print("\nSorry! You rejected to append the elemtns to teh list", end="\n")
        loopState = False
        break
    
"""
Output:
-------

Printing the total elements in the list

The element in the list index 0 is:  Cricket

The element in the list index 1 is:  football

The element in the list index 2 is:  Shuttle

The element in the list index 3 is:  Base Ball

The Reference ID of this source list is:  3239802930368

Do you want to append new element to the list (Y OR N): y

Please enter the neew element to be appended to the list: Swimming

Printing the list after appending the element:  ['Cricket', 'football', 'Shuttle', 'Base Ball', 'Swimming']

The Reference ID of this source list is:  3239802930368

Do you want to append new element to the list (Y OR N): N

Sorry! You rejected to append the elemtns to teh list
"""