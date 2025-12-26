"""
Scenario
--------
1. Given a number at runtime, confirm the number is falling under with category as "small", "medium", "large"
2. Category state is decided on the below facts
    a. small in the given number is below 10
    b. medium is the given number is below 20
    c. Any time beyond 20 is considered as large
"""

#!python3

import os
os.system("cls")

inValue01 = int(input("Please enter any numerical number: "))
print("\nthe given number is: ",inValue01,end="\n")

result = "Small" if inValue01<10 else "Medium" if inValue01<20 else "Large"
print("\nThe number is:", result,end="\n")