#!python3

import os
os.system("cls")

def getGreetings() :
    print("\nHello! This message is from Greeting function", end="\n")
    return
    
if __name__ == "__main__" :
    print("\nOperating in the global scope of the application..", end="\n")
    print("\nThe Reference address to the function is: ", getGreetings, end="\n")
    getGreetings() # this is a function call to the function "getGreetings"
    myFunctionObject = getGreetings # We are creating a clone object to the scope of the actual function getGreetings
    print("\nThe value printed by the variable \"myFunctionObject\" is: ", myFunctionObject, end="\n")
    print("\nThe operational data of \"getGreetings\" referenced in-directly using \"myFunctionObject\" is...", end="\n")
    myFunctionObject() # calling function indirectly
"""
Output:
-------
Operating in the global scope of the application..

The Reference address to the function is:  <function getGreetings at 0x000001F90F0FD940>

Hello! This message is from Greeting function

The value printed by the variable "myFunctionObject" is:  <function getGreetings at 0x000001F90F0FD940>

The operational data of "getGreetings" referenced in-directly using "myFunctionObject" is...

Hello! This message is from Greeting function

"""
    