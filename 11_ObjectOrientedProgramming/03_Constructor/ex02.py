#!python3

import os
os.system("cls")

class Sample :
    # Public data member declaration
    sampleValue = 20
    
    #Default non parametical constructor for this case
    def __init__(self):
        print("\nDefault explicit non-parametrical constructor fired...", end="\n")
        self.sampleValue = 10
        print("\nDefault explicit non-parametrical constructor completed...", end="\n")
        print("\nReturning the reference of the object to the application environment...", end="\n")

print("\nWhen the object is created, the default implicit constructor of that class will be fired...", end="\n")
print("\nHence the object is instantiated and initialized..", end="\n")
    
sampleObject = Sample()

print("\nPrinting the initial value from the object instance of sample class...")
print("\n-----------------------------oOo----------------------------------", end="\n")
print("\nThe sample object value is : ", sampleObject.sampleValue, end="\n")


print("\nPrinting the initial value from the object from the class level scope...")
print("\n-----------------------------oOo----------------------------------", end="\n")
print("\nThe value of the class level is : ", Sample.sampleValue, end="\n")
"""
Output:
-------

When the object is created, the default implicit constructor of that class will be fired...

Hence the object is instantiated and initialized..

Default explicit non-parametrical constructor fired...

Default explicit non-parametrical constructor completed...

Returning the reference of the object to the application environment...

Printing the initial value from the object instance of sample class...

-----------------------------oOo----------------------------------

The sample object value is :  10

Printing the initial value from the object from the class level scope...

-----------------------------oOo----------------------------------

The value of the class level is :  20
"""