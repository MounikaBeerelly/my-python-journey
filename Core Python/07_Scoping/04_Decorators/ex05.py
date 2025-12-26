#!python3

import time
import os
os.system("cls")

# without Decorators
def displayProfile(inUserName) :
    if inUserName.get("Authenticated") :
        return f"Hurray! Authentication is successful, Displaying the profile for {inUserName['inName']}"
    else :
        return f"Sorry! User Authentication Failed"

def authenticatedProfileDisplay(inUserName) :
    if not inUserName.get("Authenticated") :
        print("\nSorry! User is not Authenticated...", end="\n")
        return "Access Denied"
    return displayProfile(inUserName)

print("\n------- Without Decorators ---------------", end="\n")
print("\nCapturing User Details for connecting to server...", end = "\n")

inUser01 = {"inName" : "John Doe", "Authenticated" : True}
inUser02 = {"inName" : "Smith Roy", "Authenticated" : False}

print(f"\nCalling the user : {authenticatedProfileDisplay(inUser01)}", end="\n")
print(f"\nCalling the user : {authenticatedProfileDisplay(inUser02)}", end="\n")

# with Decorators

def authenticatedProfileDisplay(inFunctionName) :
    def wrapperFunction(inUserName) :
        if not inUserName.get("Authenticated") :
            print("\nSorry! User is not Authenticated...", end="\n")
            return "Access Denied"
        return inFunctionName(inUserName)
    return wrapperFunction

@authenticatedProfileDisplay
def displayProfile(inUserName) :
    return f"Hurray! Authentication is successful, Displaying the profile for {inUserName['inName']}"

print("\n------- With Decorators ---------------", end="\n")
print("\nCapturing User Details for connecting to server...", end = "\n")

inUser01 = {"inName" : "John Doe", "Authenticated" : True}
inUser02 = {"inName" : "Smith Roy", "Authenticated" : False}

print(f"\nCalling the user : {displayProfile(inUser01)}", end="\n")
print(f"\nCalling the user : {displayProfile(inUser02)}", end="\n")

"""
Output:
-------

------- Without Decorators ---------------

Capturing User Details for connecting to server...

Calling the user : Hurray! Authentication is successful, Displaying the profile for John Doe

Sorry! User is not Authenticated...

Calling the user : Access Denied

------- With Decorators ---------------

Capturing User Details for connecting to server...

Calling the user : Hurray! Authentication is successful, Displaying the profile for John Doe

Sorry! User is not Authenticated...

Calling the user : Access Denied
"""