#!python3

import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball"]

loopState = True

while loopState :
    print("\nThe Original Elements in the list are: ", listOfSports, end="\n")
    searchIndex = int(input("\nEnter the index number to search (1 to 4) :"))
   
    actualIndex = searchIndex - 1 
    
    print("\nThe sport represented in index", actualIndex, "is : ", listOfSports[actualIndex], end="\n")
    print("\nNow deleting the sport represented in index", actualIndex, end="\n")
    
    del(listOfSports[actualIndex])
            
    print("\nPrinting the updated list : ", list(listOfSports), end="\n")
    
    continueState = input("\nDo you want to continue (Yes: Y OR No: N): ")
    if continueState == 'N' or continueState == 'N' :
        print("\nYou requested for process termination...", end="\n")
        loopState = False
        
"""
Output:
-------
The Original Elements in the list are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

Enter the index number to search (1 to 4) :2

The sport represented in index 1 is :  football

Now deleting the sport represented in index 1

The deleted sport value in Index 1 is :  Shuttle

Printing the updated list :  ['Cricket', 'Shuttle', 'Base Ball']

Do you want to continue (Yes: Y OR No: N): N

You requested for process termination...
"""