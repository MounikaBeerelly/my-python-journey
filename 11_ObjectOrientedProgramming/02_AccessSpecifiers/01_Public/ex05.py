#!python3

import os
os.system("cls")

class PersonClass :
    """Class to illustrate the public attributes and public methods within the class definition promising full encapsulation"""
    personObjID = None
    personObjFirstName = None
    personObjLastName = None
    personObjDOB = None
      
    def personDataOutput(self) :
        """This is a method that is passed with an object as input at runtime for displaying the values of the variables which are outside the class"""
        print("\nAccessing the gobal variables, by using \"AttributeName\" syntax", end ="\n")
        print("\nPrinting the data from the method for variables which are outside the class", end="\n")
        print("\nThe person Allocated ID: ", self.personObjID, end="\n")
        print("\nThe person First Name: ", self.personObjFirstName, end="\n")
        print("\nThe person Last Name: ", self.personObjLastName, end="\n")
        print("\nThe person Full Name: ", self.personObjFirstName, self.personObjLastName, end="\n")
        print("\nThe person DOB: ", self.personObjDOB, end="\n")

    def personDataInput(self, inPersonObjID, inPersonObjFirstName, inPersonObjLastName, inPersonObjDOB) :
        """This is the method that is passed with an object as input at runtime for assigning the values to the variables which are outside the class"""
        print("\nBinding the attributes to the object, by calling \"AtributesNAme\" syntax", end="\n")
        self.personObjID = inPersonObjID
        self.personObjFirstName = inPersonObjFirstName
        self.personObjLastName = inPersonObjLastName
        self.personObjDOB = inPersonObjDOB
    
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

Calling the method "personDataOutput()' to update on the object "personObject01" of the Person class to show the first initialized values of the class attributes in public scope

Please enter the Person ID : 201

Please enter the Person First Name : Sachin

Please enter the Person Last Name : Tendulkar

Please enter the Person  (DD-MON_YYYY) : 19-SEP-1980

Binding the attributes to the object, by calling "AtributesNAme" syntax

Accessing the gobal variables, by using "AttributeName" syntax

Printing the data from the method for variables which are outside the class

The person Allocated ID:  201

The person First Name:  Sachin

The person Last Name:  Tendulkar

The person Full Name:  Sachin Tendulkar

The person DOB:  19-SEP-1980
"""