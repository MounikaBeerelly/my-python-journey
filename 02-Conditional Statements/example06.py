"""
Scenario:
---------
Given a number, write a program that can identify the number is Positive OR Negative, deign the logic with single liner
"""

#!python3

import os
os.system("cls")

inValue01 = int(input("\nPlease enter the numerical number: "))
print("\nThe given number is: ",inValue01,end="\n")

positiveState = "Positive" if inValue01>0 else "Negative" if inValue01<0 else "Zero"

print("\nThe given number", inValue01,"is: ",positiveState,end="\n")