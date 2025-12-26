"""
Scenario:
---------
Write a program to print all the lower case alphabetical characters of english language

Control characters: 0 to 31
Printable characters: 32 to 127
Extended ASCII: 128 to 255


Alphabetical characters
-----------------------
1. Upper case: 65 to 90
Lower case :97 to 122

Characters from range of 91 to 96
91: opening brachet
92: back slash
93: closing bracket
94. caret (^)
95: underscore
96: Grave accent (`)

"""

#!python3

import os
os.system("cls")

printChars = 97

print("\nPrinting all the alphabetical characters from \"a\"To\"z\"...",end="\n")

while(printChars <= 122):
    print("%c" %(printChars),end=" ")
    printChars = printChars + 1
    
    
#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")



