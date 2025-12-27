"""
Scenario:
---------
Given two integers write a program that can return the highest of the two numbers, Redesign the logic with single liner
"""

#!python3

import os
os.system("cls")

inValue01 = int(input("\nEnter the first number: "))
inValue02 = int(input("\nEnter the second number: "))

print("\nThe given numbers are: ",inValue01, inValue02)

highValue = inValue01 if(inValue01>inValue02) else inValue02
print("\nThe highest of the two given numbers is:",highValue,end="\n")

#outside of the "if" branch
print("Currently we are out of the \"if\" branch, operating in the main stream of the program",end="\n")