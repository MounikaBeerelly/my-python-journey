import os
os.system("cls")

#------------------ Using Normal Function -------------------
def listOfDoubles(inListElement) :
    return inListElement + inListElement

myList = [2, 4, 6, 8, 10, 15, 25]

doubledValue = map(listOfDoubles, myList)

print("\nThe reference to the doubled elements of the list pointed by the map function object is: ", doubledValue, end="\n")

finalDoubles = list(doubledValue)

print("\nThe doubled elements of the list are: ", finalDoubles, end="\n")

#------------------ Using Lambda, Map Function -------------------

myList01 = [1, 3, 5, 7, 9]

doubledValue = map(lambda element2Double : element2Double + element2Double , myList01)

print("\nThe reference to the doubled elements of the list pointed by the map function object is: ", doubledValue, end="\n")

finalDoubles = list(doubledValue)

print("\nThe doubled elements of the list are: ", finalDoubles, end="\n")

"""
Output:
-------
The reference to the doubled elements of the list pointed by the map function object is:  <map object at 0x000002E1B5598FA0>

The doubled elements of the list are:  [4, 8, 12, 16, 20, 30, 50]

The reference to the doubled elements of the list pointed by the map function object is:  <map object at 0x000002E1B5598F10>

The doubled elements of the list are:  [2, 6, 10, 14, 18]
"""