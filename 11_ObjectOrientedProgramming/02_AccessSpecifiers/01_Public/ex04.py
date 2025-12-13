#!python3

import os
os.system("cls")

class PersonClass :
    """Class to illustrate the public attributes and public methods within the class definition promising full encapsulation"""
    personObjID = 101
    personObjFirstName = "Smith"
    personObjLastName = "Roy"
    personObjDOB = "12-DEC-1990"
      
    def personDataOutput(self) :
        """This is a method that is passed with an object as input at runtime for displaying the values of the variables which are outside the class"""
        print("\nAccessing the gobal variables, by using \"AttributeName\" syntax", end ="\n")
        print("\nPrinting the data from the method for variables which are outside the class", end="\n")
        print("\nThe person Allocated ID: ", self.personObjID, end="\n")
        print("\nThe person First Name: ", self.personObjFirstName, end="\n")
        print("\nThe person Last Name: ", self.personObjLastName, end="\n")
        print("\nThe person Full Name: ", self.personObjFirstName, self.personObjLastName, end="\n")
        print("\nThe person DOB: ", self.personObjDOB, end="\n")

    def personDataInput(self) :
        """This is the method that is passed with an object as input at runtime for assigning the values to the variables which are outside the class"""
        print("\nBinding the attributes to the object, by calling \"AtributesNAme\" syntax", end="\n")
        self.personObjID = 102
        self.personObjFirstName = "John"
        self.personObjLastName = "Berkely"
        self.personObjDOB = "26-MAR-1890"
    
personObject01 = PersonClass()

print("\nCalling the method \"personDataOutput()\' to update on the object \"personObject01\" of the Person class to show the first initialized values of the class attributes in public scope", end="\n")

personObject01.personDataOutput()
personObject01.personDataInput()
personObject01.personDataOutput()

"""
Output:
------

The person First Name:  Smith

The person Last Name:  Roy

The person Full Name:  Smith Roy

The person DOB:  12-DEC-1990

Binding the attributes to the object, by calling "AtributesNAme" syntax

Accessing the gobal variables, by using "AttributeName" syntax

Printing the data from the method for variables which are outside the class

The person Allocated ID:  102

The person First Name:  John

The person Last Name:  Berkely

The person Full Name:  John Berkely

The person DOB:  26-MAR-1890

"""