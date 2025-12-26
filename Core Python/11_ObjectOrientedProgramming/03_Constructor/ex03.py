#!python3

import os
os.system("cls")

class Sample :
    # Private data member declaration
    __sampleValue = None
    
    #Default non parametical constructor for this case
    def __init__(self):
        print("\nDefault constructor is called...", end="\n")
        print("\nIntitialize the object...", end="\n")
        self.__sampleValue = 10
        print("\nInitializing the object is done successfully...", end="\n")
        print("\nDefault constructor is closed...", end="\n")

    def getData(self) :
        return self.__sampleValue

    def putData(self) :
        self.__sampleValue = int(input())
        
sampleObject = Sample()
print("\nObject creation is completed successfully...", end="\n")
print("\nPrinting the initial value from the object instance of sample class...")
print("\n-----------------------------oOo----------------------------------", end="\n")
print("\nThe sample object value is : ", sampleObject.getData(), end="\n")
print("\nPrints the initial value assigned by the constructor", end="\n")

print("\nNow scanning the value for the sample value attricute")
print("\nCalling the \"getSampleValue()\" method on the object")

print("\nPlease enter the value for the sample value : ", end="\n")
sampleObject.putData()

print("\nPrints the re-initialized value given by the call of the method", end="\n")
print("\nThe sample object value is : ", sampleObject.getData())
"""
Output:
-------
Initializing the object is done successfully...

Default constructor is closed...

Object creation is completed successfully...

Printing the initial value from the object instance of sample class...

-----------------------------oOo----------------------------------

The sample object value is :  10

Prints the initial value assigned by the constructor

Now scanning the value for the sample value attricute

Calling the "getSampleValue()" method on the object

Please enter the value for the sample value :
54

Prints the re-initialized value given by the call of the method

The sample object value is :  54
"""