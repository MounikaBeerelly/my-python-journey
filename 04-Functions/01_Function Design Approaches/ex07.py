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

def processStudentData():
    #Module to handle students information
    print("\nData input process is initializing... Please wait..",end="\n")
    
    firstName = input("\nPlease enter your first name: ")
    middleName = input("\nPlease enter your middle name: ")
    lastName = input("\nPlease enter your last name: ")
    
    print("\nData input process is completed.. Initiating the data output process.. please wait..",end="\n")
    
    print("\nThe given first name is:", firstName,end="\n")
    print("\nThe given middle name is:", middleName,end="\n")            
    print("\nThe given last name is:", lastName,end="\n")      

    print("\nData output process is completed.. Displaying the full name.. please wait..", end="\n")
    
    print("\nThe fullname is:", firstName, middleName, lastName, end="\n")
    
    return

processStudentData()
            