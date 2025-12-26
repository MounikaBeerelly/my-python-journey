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

def generateArithmeticProgression(inParam01, inParam02, inParam03, inCurrentTerm = 0) :
    if inParam03 == 0 :
        return ""
    else :
        currentTerm = inParam01 + (inParam02 * (inParam03 -1)) 
        return generateArithmeticProgression(inParam01, inParam02, inParam03 - 1) + f"{currentTerm},"
            
inParam01 = int(input("\nPlease enter the first term of the arithmetic progression: "))
inParam02 = int(input("\nPlease enter the common difference to be followed: "))
inParam03 = int(input("\nPlease enter the number of terms to be generated: "))

outResult = generateArithmeticProgression(inParam01, inParam02, inParam03)

print("\nThe Arithmetic Progression generated is: ", end="\n")
print(outResult.rstrip(", "))
 
"""
Output:
-------
Please enter the first term of the arithmetic progression: 10

Please enter the common difference to be followed: 5

Please enter the number of terms to be generated: 15

The Arithmetic Progression generated is:
10,15,20,25,30,35,40,45,50,55,60,65,70,75,80
"""