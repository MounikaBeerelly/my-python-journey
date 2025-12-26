#!python3

import os
os.system("cls")

class LeftParentClass :
    leftParentField = None
    
    def showLeftParentValue(self) :
        print("\nThe value from the Left Parent Class attribute is : ",self.leftParentField, end="\n")
        
class RightParentClass :
    rightParentField = None
    
    def showRightParentValue(self) :
        print("\nThe value from the Right Parent Class attribute is : ", self.rightParentField, end="\n")
        
class ChildClass(LeftParentClass, RightParentClass) :
    childClassField = None
    
    def showValue(self) :
        LeftParentClass.showLeftParentValue(self)
        RightParentClass.showRightParentValue(self)
        print("\nThe value from the Child class attribute is : ", self.childClassField, end="\n")
        
childClassObj = ChildClass()

print("\nAssigning value to the public atttribute of the Child class object, in reference to Parental Classes", end="\n")

childClassObj.childClassField = 10
childClassObj.leftParentField = 20
childClassObj.rightParentField = 30

print("\nCalling the public method of the Child class on the child class object", end="\n")
childClassObj.showValue()


"""
Output:
-------

Assigning value to the public atttribute of the Child class object, in reference to Parental Classes

Calling the public method of the Child class on the child class object

The value from the Left Parent Class attribute is :  20

The value from the Right Parent Class attribute is :  30

The value from the Child class attribute is :  10
"""