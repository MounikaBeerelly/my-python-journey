"""
Scenario:
---------
Write a program to print all the lower case alphabetical characters of english language
"""

#!python3

import os
os.system("cls")

printChars = "a"

print("\nPrinting all the alphabetical characters from \"a\"To\"z\"...",end="\n")

while(printChars <= "z"):
    print("%c" %(printChars),end=" ")
    printChars = chr(ord(printChars) + 1)
    
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")



