#!python3

import os
os.system("cls")

sportsList = ["Chess", "FootBall", "Shuttle", "Cricket", "Carroms", "Tennis"]

print("\nPrinting the original elements from the list : ", list(sportsList), "and the current size of the list is : ", len(sportsList), end="\n")

print("\nExecuting the pop operation upon the list, conceptually considering the list as Stack", end="\n")

popElement = sportsList.pop()

print("\nThe current popped element from the list", list(sportsList), "is : ", popElement, end="\n")
print("\nPrinting the list, after pop is executed :", list(sportsList), "And the current size of the list is :", len(sportsList), end="\n")


"""
Output:
=======
Printing the original elements from the list :  ['Chess', 'FootBall', 'Shuttle', 'Cricket', 'Carroms', 'Tennis'] and the current size of the list is :  6

Executing the pop operation upon the list, conceptually considering the list as Stack

The current popped element from the list ['Chess', 'FootBall', 'Shuttle', 'Cricket', 'Carroms'] is :  Tennis

Printing the list, after pop is executed : ['Chess', 'FootBall', 'Shuttle', 'Cricket', 'Carroms'] And the current size of the list is : 5
"""