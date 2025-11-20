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

def readStudentData():
    # The definition of the process to collect the data
    print("\nData input process is initializing... Please wait..",end="\n")
    
    firstName = input("\nPlease enter your first name: ")
    middleName = input("\nPlease enter your middle name: ")
    lastName = input("\nPlease enter your last name: ")
    
    print("\nData input process is completed.. Initiating the data output process.. please wait..",end="\n")
    writeStudentData(firstName,middleName,lastName)
    return

def writeStudentData(inFirstName,inMiddleName,inLastName):
    # The definition of the process for presenting the data
    print("\nThe given first name is:", inFirstName,end="\n")
    print("\nThe given middle name is:", inMiddleName,end="\n")            
    print("\nThe given last name is:", inLastName,end="\n")      

    print("\nData output process is completed.. Displaying the full name.. please wait..", end="\n")
    
    print("\nThe fullname is:", inFirstName, inMiddleName, inLastName, end="\n")
    return

print("\nApplication to implement the name input and output module")
print("-------------------------------", end="\n")
readStudentData()
print("\nTerminating the application...Please wait",end="\n")
            