#!python3

import os
os.system("cls")

class EmptyClass :
            pass
        
emptyClassObject = EmptyClass() 

emptyClassObject.emptyObjID = 10
emptyClassObject.emptyObjFirstName = "John"
emptyClassObject.emptyObjLastName = "Doe"
emptyClassObject.emptyObjDOB = "02-DEC-1990"

print("\nPrinting the data from the \"emptyClassObject\" object...", end="\n")
print("\nThe object ID is : ", emptyClassObject.emptyObjID, end="\n")
print("\nThe object FirstName is : ", emptyClassObject.emptyObjFirstName, end="\n")   
print("\nThe object LastName is : ", emptyClassObject.emptyObjLastName, end="\n")   
print("\nThe object Full Name is : ", emptyClassObject.emptyObjFirstName, emptyClassObject.emptyObjLastName, end="\n")   
print("\nThe object DOB is : ", emptyClassObject.emptyObjDOB, end="\n")   
   
"""
Output:
======
Printing the data from the "emptyClassObject" object...

The object ID is :  10

The object FirstName is :  John

The object LastName is :  Doe

The object Full Name is :  John Doe

The object DOB is :  02-DEC-1990
"""