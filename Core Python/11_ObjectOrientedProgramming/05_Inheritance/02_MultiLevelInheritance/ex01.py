#!python3

import os
os.system("cls")

class BaseClass :
    baseClassField = 10
    
    def showBaseClassValue(self) :
        print("\nThe value from the Base Class attribute is : ", self.baseClassField, end="\n")
        
class MiddleClass(BaseClass) :
    middleClassField = 20
    
    def showMiddleClassValue(self) :
        print("\nThe value from the Middle Class attribute is : ", self.middleClassField, end="\n")

class TerminalClass(MiddleClass) :
    terminalClassField = 30
    
    def showTerminalClassValue(self) :
        print("\nThe value from the Terminal Class attribute is : ", self.terminalClassField, end="\n")

print("\n----------Main Application Scope------------", end="\n")

terminalClassObj = TerminalClass()

print("\nCalling the public method of the Terminal Class on the Terminal Class Object..", end="\n")
terminalClassObj.showTerminalClassValue()

print("\nCalling the public method of the Middle Class on the Terminal Class Object..", end="\n")
terminalClassObj.showMiddleClassValue()

print("\nCalling the public method of the Base Class on the Terminal Class Object..", end="\n")
terminalClassObj.showBaseClassValue()

"""
Output:
------

----------Main Application Scope------------

Calling the public method of the Terminal Class on the Terminal Class Object..

The value from the Terminal Class attribute is :  30

Calling the public method of the Middle Class on the Terminal Class Object..

The value from the Middle Class attribute is :  20

Calling the public method of the Base Class on the Terminal Class Object..

The value from the Base Class attribute is :  10
"""