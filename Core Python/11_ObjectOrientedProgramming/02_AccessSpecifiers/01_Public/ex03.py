#!python3

import os
os.system("cls")

class PersonClass :
    """Class to illustrate the public attributes and public methods within the class definition promising full encapsulation"""
    personObjID = 101
    personObjFirstName = "Smith"
    personObjLastName = "Roy"
    personObjDOB = "12-DEC-1990"
      
personObject = PersonClass()

print("\nThe person Allocated ID: ", personObject.personObjID, end="\n")
print("\nThe person First Name: ", personObject.personObjFirstName, end="\n")
print("\nThe person Last Name: ", personObject.personObjLastName, end="\n")
print("\nThe person Full Name: ", personObject.personObjFirstName, personObject.personObjLastName, end="\n")
print("\nThe person DOB: ", personObject.personObjDOB, end="\n")

"""
Output:
------
The person Allocated ID:  101

The person First Name:  Smith

The person Last Name:  Roy

The person Full Name:  Smith Roy

The person DOB:  12-DEC-1990
"""