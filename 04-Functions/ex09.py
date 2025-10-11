#!python3
"""
Scenario:
---------
1. Write a program that can take the following inputs from the end user and output the given inputs with proper labels

    Inputs:
    -------
    1. First Name
    2. Middle Name
    3. Last Name
    4. Full Name
"""
import os
os.system("cls")

def giveFirstName():
    # module definition to accept the first name from the end user
        firstName = input("\nPlease enter your first name: ")
        return firstName
def giveMiddleName():
    # module definition to accept the middle name from the end user
        middleName = input("\nPlease enter your middle name: ")
        return middleName 

def giveLastName():
    # module definition to accept the last name from the end user
        lastName = input("\nPlease enter your last name: ")
        return lastName

def writeStudentData(firstName,middleName,lastName):
    # The definition of the process for presenting the data
    print("\nThe given first name is:", firstName,end="\n")
    print("\nThe given middle name is:", middleName,end="\n")            
    print("\nThe given last name is:", lastName,end="\n")      

    print("\nData output process is completed.. Displaying the full name.. please wait..", end="\n")
    
    print("\nThe fullname is:", firstName, middleName, lastName, end="\n")
    return

print("\nApplication to implement the name input and output module")
print("-------------------------------", end="\n")

firstName = giveFirstName()
middleName = giveMiddleName()
lastName = giveLastName()

print("\nCalling the module for printing the end users given details.. please wait..",end="\n")

writeStudentData(firstName, middleName, lastName)

print("\nTerminating the application...Please wait",end="\n")
            