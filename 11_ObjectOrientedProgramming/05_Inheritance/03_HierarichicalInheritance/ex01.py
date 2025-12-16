#!python3

import os
os.system("cls")

class BaseClass :
    baseClassField = None
    
    def showBaseValue(self):
        print("\nThe value from the Base Class Attribute is : ",self.baseClassField, end="\n")
        
class LeftChildClass(BaseClass) :
    leftchildField = None
    
    def showLeftChildValue(self):
        print("\nThe value from the Left Child Class Attribute is : ",self.leftchildField, end="\n")
           
class RightChildClass(BaseClass) :
    rightchildField = None
    
    def showRightChildValue(self):
        print("\nThe value from the Right Child Class Attribute is : ",self.rightchildField, end="\n")
           
leftChildClassObj = LeftChildClass()

print("\nAssigning value to the public attribute of the BaseClass using the object of the LeftchildClass", end = "\n")
leftChildClassObj.baseClassField = 15

print("\nAssigning value to the public attribute of the Left Child Class using the object of the LeftchildClass", end = "\n")
leftChildClassObj.leftchildField = 40

print("\nCalling the public Method of the BaseClass using the object of the LeftchildClass", end = "\n")
leftChildClassObj.showBaseValue()

print("\nCalling the public method of the Left Child Class using the object of the LeftchildClass", end = "\n")
leftChildClassObj.showLeftChildValue()

rightChildClassObj = RightChildClass()

print("\nAssigning value to the public attribute of the BaseClass using the object of the RightchildClass", end = "\n")
rightChildClassObj.baseClassField = 20

print("\nAssigning value to the public attribute of the Right Child Class using the object of the RightchildClass", end = "\n")
rightChildClassObj.rightchildField = 50

print("\nCalling the public Method of the BaseClass using the object of the rightChildClass", end = "\n")
rightChildClassObj.showBaseValue()

print("\nCalling the public method of the Right Child Class using the object of the RightChildClass", end = "\n")
rightChildClassObj.showRightChildValue()


"""
Output:
-------

Assigning value to the public attribute of the BaseClass using the object of the LeftchildClass

Assigning value to the public attribute of the Left Child Class using the object of the LeftchildClass

Calling the public Method of the BaseClass using the object of the LeftchildClass

The value from the Base Class Attribute is :  15

Calling the public method of the Left Child Class using the object of the LeftchildClass

The value from the Left Child Class Attribute is :  40

Assigning value to the public attribute of the BaseClass using the object of the RightchildClass

Assigning value to the public attribute of the Right Child Class using the object of the RightchildClass

Calling the public Method of the BaseClass using the object of the rightChildClass

The value from the Base Class Attribute is :  20

Calling the public method of the Right Child Class using the object of the RightChildClass

The value from the Right Child Class Attribute is :  50
"""
