"""
Scenario:
---------
1. Write a program to generate the following output

Line 1 Output is 1
Line 2 Output is 2
Line 3 Output is 3
Line 4 Output is 4
Line 5 Output is 5
"""

#!python3

import os
os.system("cls")

print("\nIllustration of\"WHILE\" loop in python")
print("------------OoO----------",end="\n")

loopControl = 1 #loop initialization statement

print("\nInitializing the loop for execution...Please wait...",end="\n")

while(loopControl <= 5): #loop conditional statement
    print("Line",loopControl,"Output is",loopControl,end="\n") #Loop action statement
    loopControl = loopControl + 1 #Loop updation statement
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")


"""
Scenario:
---------
Write a program to generate sequence of numbers from 1 to 5
"""

print("\nThe sequence of numbers from 1 to 5 are...",end="\n")

loopControl01 = 1

while(loopControl01 <= 5):
    print(loopControl01,end=",")
    loopControl01 = loopControl01+1