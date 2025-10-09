"""
Scenario:
---------
1. The system of the employment registration department wants to check the following validations before any person is registering for an employee program.
    a. The program should prompt the end user for "Input of the current age" of the candidate.
    b. Display the given age to the console.
    c. Check the validation for allowing only tthose candidates as eligible for the employment program, if they are only above 18 years of age, and display a proper message for acceptance.
    d. For all the candidates whose age is within the range of 0 years to 18 years, Reject the registration process by a meaningful message.
"""

#!python3

import os
os.system("cls")

inAge = int(input("\nPlease enter your current age: "))
print("\nThe given age is:",inAge,"Years.",end="\n")

if inAge >= 0 and inAge <= 18:
    print("\nSorry! You are not eligible for seeking employment", end="\n")
    print("\nYou have to wait for more:",(18-inAge),"Years, to seek your employment", end="\n")
    print("\nPlease register yourself for Un-Employment Aid Scheme from the government", end="\n")
else:
    print("\nCongratulations! You ar eligible for seeking employment. Please forward your latest resume.", end="\n")