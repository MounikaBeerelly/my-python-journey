#!python3

import os
os.system("cls")

# Defining the List
listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

loopState = True

while loopState :
    os.system("cls")
    print("\nThe original elements in the list are: ", listOfNumbers, end="\n")
    
    slicePointer = int(input("\nPlease enter the position for slicing : "))
    nElements = int(input("\nPlease enter the number of elements to slice : "))

    print("\n------------------oOo----------------", end="\n")
    print("\nThe applied position int he list is : ", slicePointer, end="\n")
    print("\nThe number of elements requested : ", nElements, end="\n")
    
    print("\nThe sliced elements are : ", listOfNumbers[slicePointer : (slicePointer + nElements)], end= "\n")
    
    continueState = input("\nDo you want to continue (Yes: Y OR No: N): ")
    if continueState == 'N' or continueState == 'N' :
        print("\nYou requested for process termination...", end="\n")
        loopState = False
        
"""
Output:
-------

The original elements in the list are:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

Please enter the position for slicing : 3

Please enter the number of elements to slice : 5

------------------oOo----------------

The applied position int he list is :  3

The number of elements requested :  5

The sliced elements are :  [4, 5, 6, 7, 8]

Do you want to continue (Yes: Y OR No: N): N

You requested for process termination...

"""