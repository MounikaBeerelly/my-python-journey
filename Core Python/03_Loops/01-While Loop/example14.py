"""
Scenario:
---------
Write a program to accept any number from the end user and implement the logic for Palindrome

- Do not use any existing python modules OR libraries OR built-in functions
"""

#!python3

import os
os.system("cls")

inNumber = reverseNumber = originalNumber = reminder = 0

inNumber = int(input("\nenter the required number to reverse:"))

originalNumber = inNumber 

while(inNumber != 0):
    reminder = inNumber % 10
    reverseNumber = int((reverseNumber * 10) + reminder)
    inNumber = int(inNumber/10)
    
print("\nThe given number %d Reverse will be %d"%(originalNumber,reverseNumber),end="\n")

if(originalNumber == reverseNumber):
    print("\nThe given number %d is Palindrome:%d"%(originalNumber,reverseNumber),end="\n")
else:
    print("\nThe given number %d is not a Palindrome:%d"%(originalNumber,reverseNumber),end="\n")