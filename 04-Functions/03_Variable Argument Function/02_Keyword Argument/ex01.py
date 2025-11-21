#!python3

import os
os.system("cls")

def printKWArgs(**kwargs) :
    print("\nThe given keyword arguments are..", end="\n")
    print(kwargs)
    return

print("\nThis is the main module..", end="\n")
print("---------------------------", end="\n")

printKWArgs(FirstName = "Smith", LastName = "Roy", Age = 31, Height = 135.23, Place = "Hyderabad")


"""
Output:
=======
This is the main module..
---------------------------

The given keyword arguments are..
{'FirstName': 'Smith', 'LastName': 'Roy', 'Age': 31, 'Height': 135.23, 'Place': 'Hyderabad'}
"""