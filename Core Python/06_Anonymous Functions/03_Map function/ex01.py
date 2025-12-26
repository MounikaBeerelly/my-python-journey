import os
os.system("cls")

#------------------ Using Normal Function -------------------
def listOfSquares(inListElement) :
    return inListElement * inListElement

myList = [2, 4, 6, 8, 10, 15, 25]

squaredValue = map(listOfSquares, myList)

print("\nThe reference to the squared elements of the list pointed by the map function object is: ", squaredValue, end="\n")

finalSquares = list(squaredValue)

print("\nThe squared elements of the list are: ", finalSquares, end="\n")

#------------------ Using Lambda, Map Function -------------------

myList01 = [1, 3, 5, 7, 9]

squaredValue = map(lambda element2Square : element2Square * element2Square , myList01)

print("\nThe reference to the squared elements of the list pointed by the map function object is: ", squaredValue, end="\n")

finalSquares = list(squaredValue)

print("\nThe squared elements of the list are: ", finalSquares, end="\n")

"""
Output:
-------
The reference to the squared elements of the list pointed by the map function object is:  <map object at 0x0000022D2B528FA0>

The squared elements of the list are:  [4, 16, 36, 64, 100, 225, 625]

The reference to the squared elements of the list pointed by the map function object is:  <map object at 0x0000022D2B528F10>

The squared elements of the list are:  [1, 9, 25, 49, 81]
"""