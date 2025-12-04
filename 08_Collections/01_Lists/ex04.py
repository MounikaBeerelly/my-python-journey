#!python3

import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball"]

loopState = True

while loopState :
    print("\nThe Original Elements in the list are: ", listOfSports, end="\n")
    searchIndex = int(input("\nEnter the index number to search (0 to 3) :"))
    
    print("\nThe sport represented in index", searchIndex, "is : ", listOfSports[searchIndex], end="\n")
    print("\nNow updating the sport represented in index", searchIndex, end="\n")
    
    newValue = input("\nPlease enter the value to update :")
    
    listOfSports[searchIndex] = newValue
    
    print("\nThe updated sport value in Index", searchIndex, "is : ", listOfSports[searchIndex], end="\n")
    print("\nPrinting the updated list : ", list(listOfSports), end="\n")
    
    continueState = input("\nDo you want to continue (Yes: Y OR No: N): ")
    if continueState == 'N' or continueState == 'N' :
        print("\nYou requested for process termination...", end="\n")
        loopState = False
        
"""
Output:
-------
The Original Elements in the list are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

Enter the index number to search (0 to 3) :1

The sport represented in index 1 is :  football

Now updating the sport represented in index 1

Please enter the value to update :Tennis

The updated sport value in Index 1 is :  Tennis

Printing the updated list :  ['Cricket', 'Tennis', 'Shuttle', 'Base Ball']

Do you want to continue (Yes: Y OR No: N): N

You requested for process termination...
"""