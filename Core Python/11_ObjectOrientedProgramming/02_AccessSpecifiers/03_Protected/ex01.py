#!python3

import os
os.system("cls")

class PersonClass :
    """Class to illustrate the protected attributes and public methods within the class definition promising full encapsulation"""
    _personObjID = None
    _personObjFirstName = None
    _personObjLastName = None
    _personObjDOB = None
      
    def personDataOutput(self) :
        """This is a method that is passed with an object as input at runtime for displaying the values of the variables which are outside the class"""
        print("\nAccessing the gobal variables, by using \"AttributeName\" syntax", end ="\n")
        print("\nPrinting the data from the method for variables which are outside the class", end="\n")
        print("\nThe person Allocated ID: ", self._personObjID, end="\n")
        print("\nThe person First Name: ", self._personObjFirstName, end="\n")
        print("\nThe person Last Name: ", self._personObjLastName, end="\n")
        print("\nThe person Full Name: ", self._personObjFirstName, self._personObjLastName, end="\n")
        print("\nThe person DOB: ", self._personObjDOB, end="\n")

    def personDataInput(self, inPersonObjID, inPersonObjFirstName, inPersonObjLastName, inPersonObjDOB) :
        """This is the method that is passed with an object as input at runtime for assigning the values to the variables which are outside the class"""
        print("\nBinding the attributes to the object, by calling \"AtributesNAme\" syntax", end="\n")
        self._personObjID = inPersonObjID
        self._personObjFirstName = inPersonObjFirstName
        self._personObjLastName = inPersonObjLastName
        self._personObjDOB = inPersonObjDOB
    
personObject01 = PersonClass()

print("\nCalling the method \"personDataOutput()\' to update on the object \"personObject01\" of the Person class to show the first initialized values of the class attributes in public scope", end="\n")

personObjID = int(input("\nPlease enter the Person ID : "))
personObjFirstName = input("\nPlease enter the Person First Name : ")
personObjLastName = input("\nPlease enter the Person Last Name : ")
personObjDOB = input("\nPlease enter the Person  (DD-MON_YYYY) : ")

personObject01.personDataInput(personObjID, personObjFirstName, personObjLastName, personObjDOB)
personObject01.personDataOutput()

"""
Output:
------

Please enter the Person ID : 10

Please enter the Person First Name : John

Please enter the Person Last Name : Doe

Please enter the Person  (DD-MON_YYYY) : 12-SEP-1880

Binding the attributes to the object, by calling "AtributesNAme" syntax

Accessing the gobal variables, by using "AttributeName" syntax

Printing the data from the method for variables which are outside the class

The person Allocated ID:  10

The person First Name:  John

The person Last Name:  Doe

The person Full Name:  John Doe

The person DOB:  12-SEP-1880

"""