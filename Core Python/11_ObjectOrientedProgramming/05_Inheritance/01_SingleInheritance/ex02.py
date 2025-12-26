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
    def setValue(self) :
        baseClassMessageChoice = input("\nDo you want to initiate the Base Class Members [Y: Yes OR N:No] : ")
        if(baseClassMessageChoice == 'Y' or baseClassMessageChoice == 'y') :
            print("\nAssigning the data to the Base Class Level using Message PAssing...", end="\n")
            inBaseDerivedValue = int(input("\nPlease enter the value for the Base Class Level : "))
            super().setBaseClassField(inBaseDerivedValue)
            print("\nAssigning the data to the Derived Class object...", end="\n")
            inDerivedValue = int(input("\nPlease enter the value for the Derived Class object : "))
            self.__derivedClassField = inDerivedValue
        else : 
            print("\nAssigning the data to the Derived Class object...", end="\n")
            inDerivedValue = int(input("\nPlease enter the value for the Derived Class object : "))
            self.__derivedClassField = inDerivedValue
        return baseClassMessageChoice
    
    def getValue(self, inBaseClassState) :
        # Getter for the private attribute of the Derived Class attribute
        if(inBaseClassState == 'y' or inBaseClassState == 'Y') :
            print("\nAccessing the data from the Base Class Level using the Derived Class object...", end="\n")
            baseClassObjValue = super().getBaseClassField()
            print("\nThe data assigned to Base Class Object attribute : %d" %(baseClassObjValue), end="\n")
            print("\nAccessing the data from the Derived Class object...", end="\n")
            print("\nThe data assigned to Derived Class Object attribute : %d" %(self.__derivedClassField), end="\n")
        else :
            print("\nAccessing the data from the Derived Class object...", end="\n")
            print("\nThe data assigned to Derived Class Object attribute : %d" %(self.__derivedClassField), end="\n")
        return

print("\n---------MainApplication with Derived Class----------", end="\n")
print("\nCreating the Derived class Instance as an Object...", end="\n")
derivedClassObj = DerivedClass()
print('\n----Operating by calling the Base class methods on Derived class objects----', end="\n")
baseClassState = derivedClassObj.setValue()

derivedClassObj.getValue(baseClassState)


"""
Output:
-------

---------MainApplication with Derived Class----------

Creating the Derived class Instance as an Object...

----Operating by calling the Base class methods on Derived class objects----

Do you want to initiate the Base Class Members [Y: Yes OR N:No] : y

Assigning the data to the Base Class Level using Message PAssing...

Please enter the value for the Base Class Level : 76

Assigning the data to the Derived Class object...

Please enter the value for the Derived Class object : 98

Accessing the data from the Base Class Level using the Derived Class object...

The data assigned to Base Class Object attribute : 76

Accessing the data from the Derived Class object...

The data assigned to Derived Class Object attribute : 98
"""