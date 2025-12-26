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
"""