#!python3

import os
os.system("cls")

class PersonClass :
    """Class to illustrate the private attributes and public methods within the class definition promising full encapsulation"""
    __personObjID = None
    __personObjFirstName = None
    __personObjLastName = None
    __personObjDOB = None
      
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
        self.__personObjID = inPersonObjID
        self.__personObjFirstName = inPersonObjFirstName
        self.__personObjLastName = inPersonObjLastName
        self.__personObjDOB = inPersonObjDOB
    
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

Please enter the Person ID : 101

Please enter the Person First Name : Smith

Please enter the Person Last Name : Roi

Please enter the Person  (DD-MON_YYYY) : 04-OCT-1990

Binding the attributes to the object, by calling "AtributesNAme" syntax

Accessing the gobal variables, by using "AttributeName" syntax

Printing the data from the method for variables which are outside the class

The person Allocated ID:  101

The person First Name:  Smith

The person Last Name:  Roi

The person Full Name:  Smith Roi

The person DOB:  04-OCT-1990
"""