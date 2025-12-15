#!python3

import os
os.system("cls")

class PersonClass :
    """Class to illustrate the private attributes and public methods within the class definition promising full encapsulation"""
    __personObjID = 101
    __personObjFirstName = "Smith"
    __personObjLastName = "Roy"
    __personObjDOB = "12-DEC-1990"
      
      
    def personDataOutput(self) :
        """This is a method that is passed with an object as input at runtime for displaying the values of the variables which are outside the class"""
        print("\nAccessing the gobal variables, by using \"AttributeName\" syntax", end ="\n")
        print("\nPrinting the data from the method for variables which are outside the class", end="\n")
        print("\nThe person Allocated ID: ", self.__personObjID, end="\n")
        print("\nThe person First Name: ", self.__personObjFirstName, end="\n")
        print("\nThe person Last Name: ", self.__personObjLastName, end="\n")
        print("\nThe person Full Name: ", self.__personObjFirstName, self.__personObjLastName, end="\n")
        print("\nThe person DOB: ", self.__personObjDOB, end="\n")

    def personDataInput(self, inPersonObjID, inPersonObjFirstName, inPersonObjLastName, inPersonObjDOB) :
        """This is the method that is passed with an object as input at runtime for assigning the values to the variables which are outside the class"""
        print("\nBinding the attributes to the object, by calling \"AtributesNAme\" syntax", end="\n")
        self.personObjID = inPersonObjID
        self.personObjFirstName = inPersonObjFirstName
        self.personObjLastName = inPersonObjLastName
        self.personObjDOB = inPersonObjDOB
    
personObject01 = PersonClass()

print("\nCalling the method \"personDataOutput()\' to update on the object \"personObject01\" of the Person class to show the first initialized values of the class attributes in public scope", end="\n")

personObject01.personDataOutput()

"""
Output:
------
Calling the method "personDataOutput()' to update on the object "personObject01" of the Person class to show the first initialized values of the class attributes in public scope

Accessing the gobal variables, by using "AttributeName" syntax

Printing the data from the method for variables which are outside the class

The person Allocated ID:  101

The person First Name:  Smith

The person Last Name:  Roy

The person Full Name:  Smith Roy

The person DOB:  12-DEC-1990
"""