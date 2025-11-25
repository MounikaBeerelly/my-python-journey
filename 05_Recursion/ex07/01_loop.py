"""
Scenario:
---------
Write a program to generate Arithmetic Progression Series using Recursion
Arithmetic Progression:
-----------------------
1. Arithmetic Progression, OR AP, is a sequence of numbers in which the difference of any two successive members is a constant
2. This constant difference is called the "common difference"

General  Illustration: 2, 5, 8, 11, 14
"""

import os
import sys
os.system("cls")

inParam01 = int(input("\nPlease enter the first term of the arithmetic progression: "))
inParam02 = int(input("\nPlease enter the common difference to be followed: "))
inParam03 = int(input("\nPlease enter the number of terms to be generated: "))

print("\nThe Arithmetic Progression generated is: ", end="\n")

for loopIndex in range(1, inParam03 + 1) :
    currentTerm = inParam01 + (loopIndex -1) * inParam02
    print("%d,  "%(currentTerm), end="")

print()
 
"""
Output:
-------
Please enter the first term of the arithmetic progression: 10

Please enter the common difference to be followed: 3

Please enter the number of terms to be generated: 10

The Arithmetic Progression generated is:
10,  13,  16,  19,  22,  25,  28,  31,  34,  37,
"""