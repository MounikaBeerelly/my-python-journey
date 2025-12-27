"""
Scenario:
---------
Write a program to print all the existing even numbers in a range as given by the end user
"""

#!python3

import os
os.system("cls")

initialValue = int(input("\nPlease enter the initial value to operate:"))
finalValue = int(input("Pleas enter the final value to operate:"))

print("\nPrinting the even number from %d"%(initialValue),"To %d"%(finalValue),"...",end="\n")

while(initialValue <= finalValue):
    if(initialValue % 2 == 0):
        print("%d" %(initialValue),end=" ")
    initialValue = initialValue + 1
    
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")



