#!python3

import os
os.system("cls")

class Sample :
    # Private data member declaration
    __sampleValue = None
    
    #Default non parametical constructor for this case
    def __init__(self, inSampleValue):
        print("\nDefault constructor is called...", end="\n")
        print("\nIntitialize the object...", end="\n")
        self.__sampleValue = inSampleValue
        print("\nInitializing the object is done successfully...", end="\n")
        print("\nDefault constructor is closed...", end="\n")

    def getData(self) :
        return self.__sampleValue
    
    def __del__(self) : #Pythons destructor methos, called when the reference to the object is about to lost
        print("\n------------Destructor Initiated--------------", end="\n")
        print("\nDstructor is called..", end="\n")
        print("\nInitiating the process for Object Deletion...", end="\n")
        print("\nObject destruction is done successfully..", end="\n")
        print("\nDestructor is Terminated successfully...", end="\n")
        print("\n------Destructor Terminated-----------", end="\n")
        
sampleObject01 = Sample(10)
print("\nPrinting the initial value from the object instance of sample class...")
print("\n-----------------------------oOo----------------------------------", end="\n")
print("\nThe sample object value is : ", sampleObject01.getData(), end="\n")

sampleObject02 = Sample(25)
print("\nPrinting the initial value from the object instance of sample class...")
print("\n-----------------------------oOo----------------------------------", end="\n")
print("\nThe sample object value is : ", sampleObject02.getData(), end="\n")


"""
Output:
-------

Default constructor is called...

Intitialize the object...

Initializing the object is done successfully...

Default constructor is closed...

Printing the initial value from the object instance of sample class...

-----------------------------oOo----------------------------------

The sample object value is :  10

Default constructor is called...

Intitialize the object...

Initializing the object is done successfully...

Default constructor is closed...

Printing the initial value from the object instance of sample class...

-----------------------------oOo----------------------------------

The sample object value is :  25

------------Destructor Initiated--------------

Dstructor is called..

Initiating the process for Object Deletion...

Object destruction is done successfully..

Destructor is Terminated successfully...

------Destructor Terminated-----------

------------Destructor Initiated--------------

Dstructor is called..

Initiating the process for Object Deletion...

Object destruction is done successfully..

Destructor is Terminated successfully...

------Destructor Terminated-----------
"""