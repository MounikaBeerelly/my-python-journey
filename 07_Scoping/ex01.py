#!python3

# The global scope of the Python application begins here
import os # Global scope
os.system("cls") # "system" function is built-in scope

myGlobalVar = 45 # global variable

def outerFunction() : 
    # Local scope of the outer function is begins here
    print("\n---------Outer Function-------------")
    print(f"\nThe value in the variable \"myGlobalVar\" is : {myGlobalVar} : Used in the global scope influence", end="\n")
    myOuterVar = 55
    print(f"\nThe value in the variable \"myOuterVar\" is : {myOuterVar} : Used in the local scope influence", end="\n")
    
    def innerFunction() :
        # Local scope of the inner function is begins here
        myInnerVar = 65
        print("\n---------Inner Function-------------")
        print(f"\nThe value in the variable \"myInnerVar\" is : {myInnerVar} : Used in the local scope influence", end="\n")
        print(f"\nThe value in the variable \"myOuterVar\" is : {myOuterVar} : Used in the Enclosing scope influence", end="\n")
        print(f"\nThe value in the variable \"myGlobalVar\" is : {myGlobalVar} : Used in the global scope influence", end="\n")
        return 
        # Local scope of the inner function is ends here
    
    innerFunction()
    return 
    # Local scope of the outer function is ends here
print("\n---------Global Scope-------------")
print(f"\nThe value at the Global Scope level - {myGlobalVar}", end="\n")
outerFunction()

# The global scope of the Python application ends here

"""
Output:
======
---------Global Scope-------------

The value at the Global Scope level - 45

---------Outer Function-------------

The value in the variable "myGlobalVar" is : 45 : Used in the global scope influence

The value in the variable "myOuterVar" is : 55 : Used in the local scope influence

---------Inner Function-------------

The value in the variable "myInnerVar" is : 65 : Used in the local scope influence

The value in the variable "myOuterVar" is : 55 : Used in the Enclosing scope influence

The value in the variable "myGlobalVar" is : 45 : Used in the global scope influence
"""