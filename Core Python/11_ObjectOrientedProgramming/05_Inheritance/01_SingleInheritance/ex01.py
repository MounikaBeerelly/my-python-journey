#!python3

import os
os.system("cls")

class BaseClass :
    __baseClassField = None
    
    def setBaseClassField(self, inParamValue) :
        # Setter for the private attributes of the Base class field
        self.__baseClassField = inParamValue
        return
    
    def getBaseClassField(self) :
        # Getter for the private class of the Base Class Field
        return self.__baseClassField
    
#Implementing the Single Inheritance in Python 
class DerivedClass(BaseClass) :
    __derivedClassField = None
    
    def setDerivedClassField(self, inParamValue) :
        # Setter for the private attributes of the Derived class field
        self.__derivedClassField = inParamValue
        return
    
    def getDerivedClassField(self) :
        # Getter for the private class of the Derived Class Field
        return self.__derivedClassField
    
print("\n----------Main application with Base Class-------------------", end="\n")
print("\nCreating Base Class Instance as an object...", end="\n")
baseClassObj = BaseClass()
print("\nAssigning the data to the Base Class object...", end="\n")
inBaseValue = int(input("\nPlease enter the value for the Base Class object : "))
baseClassObj.setBaseClassField(inBaseValue)

print("\nAccessing the data from the Base Class object...", end="\n")
baseClassObjValue = baseClassObj.getBaseClassField()
print("\nThe data assigned to Base Class Object attribute : %d" %(baseClassObjValue), end="\n")

print("\n----------Main application with Derived Class-------------------", end="\n")
print("\nCreating Derived Class Instance as an object...", end="\n")
derivedClassObj = DerivedClass()
print("\nAssigning the data to the Derived Class object...", end="\n")
inDerivedValue = int(input("\nPlease enter the value for the Derived Class object : "))
derivedClassObj.setDerivedClassField(inDerivedValue)

print("\nAccessing the data from the Derived Class object...", end="\n")
derivedClassObjValue = derivedClassObj.getDerivedClassField()
print("\nThe data assigned to Derived Class Object attribute : %d" %(derivedClassObjValue), end="\n")

"""
Output:
-------

----------Main application with Base Class-------------------

Creating Base Class Instance as an object...

Assigning the data to the Base Class object...

Please enter the value for the Base Class object : 11

Accessing the data from the Base Class object...

The data assigned to Base Class Object attribute : 11

----------Main application with Derived Class-------------------

Creating Derived Class Instance as an object...

Assigning the data to the Derived Class object...

Please enter the value for the Derived Class object : 76

Accessing the data from the Derived Class object...

The data assigned to Derived Class Object attribute : 76
"""