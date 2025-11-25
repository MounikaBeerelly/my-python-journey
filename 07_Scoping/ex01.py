#!python3

# The global scope of the Python application begins here
import os # Global scope
os.system("cls") # "system" function is built-in scope

def raiseValue(inbaseValue) :  # Global scope
    # Local scope of the current function is begins here
    finalResult = inbaseValue ** 2
    print(f"The square of the {inbaseValue} is: {finalResult}", end="\n")
    return 
    # Local scope of the current function is ends here

print("\nMain scope of the application begins from here", end="\n")
inValue = int(input("\nPlease enter the required value: "))
raiseValue(inValue)

print("\nThe raised value of  ", inValue, " is :",end="\n" )

# The global scope of the Python application ends here

"""
Output:
======

"""