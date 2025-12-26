#!python3

import os
os.system("cls")

class Sample :
    # Public data member declaration
    sampleValue = None
    
    #Default non parametical constructor for this case
    def __init__(self):
        print("\nDefault explicit non-parametrical constructor fired...", end="\n")
        self.sampleValue = 10
        print("\nDefault explicit non-parametrical constructor completed...", end="\n")
        print("\nReturning the reference of the object to the application environment...", end="\n")

print("\nWhen the object is created, the default implicit constructor of that class will be fired...", end="\n")
print("\nHence the object is instantiated and initialized..", end="\n")
    
sampleObject = Sample()

print("\nPrinting the initial value from the object instance of sample data...")
print("\n-----------------------------oOo----------------------------------", end="\n")
      
print("\nThe sample object value is : ", sampleObject.sampleValue, end="\n")


"""
Output:
-------

When the object is created, the default implicit constructor of that class will be fired...

Hence the object is instantiated and initialized..

Default explicit non-parametrical constructor fired...

Default explicit non-parametrical constructor completed...

Returning the reference of the object to the application environment...

Printing the initial value from the object instance of sample data...

-----------------------------oOo----------------------------------

The sample object value is :  10
"""