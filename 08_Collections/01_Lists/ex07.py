#!python3

from tabulate import tabulate
import os
os.system("cls")

# Defining the List
listOfSports = ["Cricket", "football", "Shuttle", "Base Ball"]

print("--------------Approach 01--------------")
print("\nThe Original identified Sports are: ", listOfSports, end="\n")
 
print("\n--------------Approach 02--------------")
print("\nThe Original identified Sports are: ", list(listOfSports), end="\n")
 
print("\n--------------Approach 03--------------")
loopCounter = 0
while(loopCounter < len(listOfSports)) :
    print("\nThe element in Index", loopCounter, " is: ", listOfSports[loopCounter], end="\n")
    loopCounter += 1

print("\n--------------Approach 04--------------")

print("\nThe total length of the List is: ", len(listOfSports), end="\n")
print("\nPrinting the total elements in the list..", end="\n")
print("\nIndex\t|\tElement")
print("-------------------")
for itemIndex, itemValue in enumerate(listOfSports, 1) :
    print(f"{itemIndex}\t|\t{itemValue}")
    
print("\n--------------Approach 05--------------")

sportaTable = [["Index", "Sport"]] + [[indexValue + 1, sportItem] for indexValue, sportItem in enumerate(listOfSports)]
print(tabulate(sportaTable, headers = "firstrow", tablefmt = "grid"))
"""
Output:
-------
--------------Approach 01--------------

The Original identified Sports are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

--------------Approach 02--------------

The Original identified Sports are:  ['Cricket', 'football', 'Shuttle', 'Base Ball']

--------------Approach 03--------------

The element in Index 0  is:  Cricket

The element in Index 1  is:  football

The element in Index 2  is:  Shuttle

The element in Index 3  is:  Base Ball

--------------Approach 04--------------

The total length of the List is:  4

Printing the total elements in the list..

Index   |       Element
-------------------
1       |       Cricket
2       |       football
3       |       Shuttle
4       |       Base Ball

--------------Approach 05--------------
+---------+-----------+
|   Index | Sport     |
+=========+===========+
|       1 | Cricket   |
+---------+-----------+
|       2 | football  |
+---------+-----------+
|       3 | Shuttle   |
+---------+-----------+
|       4 | Base Ball |
+---------+-----------+
"""