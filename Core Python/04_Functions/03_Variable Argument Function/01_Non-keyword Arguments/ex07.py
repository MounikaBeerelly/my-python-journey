#!python3

import os
os.system("cls")

def captureData(*args) :
    # function to capture the data dynamically at runtime with different types
    for caturedValueIndex in args :
        print("\nThe currently captured value is: ", caturedValueIndex, end="\n")
    return

print("\nThis is the main module", end="\n")
print("-------------------------", end="\n")

firstName = input("\nPlease enter your first name: ")
middleName = input("\nPlease enter your middle name: ")
lastName = input("\nPlease enter your last name: ")
print("\nCalling the function with my Personal Information..", end="\n")
print("-----------------------------------------------------", end="\n")
captureData(firstName, middleName, lastName)

houseNumber = input("\nPlease enter your House number: ")
floorNumber = input("\nPlease enter your Floor Number: ")
buildingNumber = input("\nPlease enter your Building number: ")
streetName = input("\nPlease enter your Street name: ")
cityName = input("\nPlease enter your City name: ")
stateName = input("\nPlease enter your State name: ")
countryName = input("\nPlease enter your Country name: ")
print("\nCalling the function with my Address Information..", end="\n")
print("----------------------------------------------------", end="\n")
captureData(houseNumber, floorNumber, buildingNumber, streetName, cityName, stateName, countryName)

mobileNumber = input("\nPlease enter your Mobile number: ")
mailID = input("\nPlease enter your Mail ID: ")
print("\nCalling the function with my Communication Information..", end="\n")
print("----------------------------------------------------", end="\n")
captureData(mobileNumber, mailID)

"""
Output:
-------

This is the main module
-------------------------

Please enter your first name: Smith

Please enter your middle name: Roy

Please enter your last name: B

Calling the function with my Personal Information..
-----------------------------------------------------

The currently captured value is:  Smith

The currently captured value is:  Roy

The currently captured value is:  B

Please enter your House number: 2-32

Please enter your Floor Number: 4th

Please enter your Building number: 102

Please enter your Street name: Q - street

Please enter your City name: Hyderabad

Please enter your State name: Telangana

Please enter your Country name: India

Calling the function with my Address Information..
----------------------------------------------------

The currently captured value is:  2-32

The currently captured value is:  4th

The currently captured value is:  102

The currently captured value is:  Q - street

The currently captured value is:  Hyderabad

The currently captured value is:  Telangana

The currently captured value is:  India

Please enter your Mobile number: 1234431234

Please enter your Mail ID: smith@gmail.com

Calling the function with my Communication Information..
----------------------------------------------------

The currently captured value is:  1234431234

The currently captured value is:  smith@gmail.com
"""