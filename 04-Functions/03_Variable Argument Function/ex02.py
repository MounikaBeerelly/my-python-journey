#!python3

import time

import os
os.system("cls")

def stringMaker(*args) :
   #function to concatenate the give words into a single string
   print("\nThe given parameters from the end user is:", args, end="\n")
   return " ".join(args)

print("\nThe main application begins here...", end="\n")

print("\nThe given words are \"Hello\", \"World\", concatenated as: ", stringMaker("Hello", "World"), end="\n")
print("\nThe given words are \"Python\", \"rules\", \"the\", \"Market\", concatenated as: ", stringMaker("Python", "Rules", "the", "Market"), end="\n") 
 
    
"""
Output:
-------
The main application begins here...

The given parameters from the end user is: ('Hello', 'World')

The given words are "Hello", "World", concatenated as:  Hello World

The given parameters from the end user is: ('Python', 'Rules', 'the', 'Market')

The given words are "Python", "rules", "the", "Market", concatenated as:  Python Rules the Market
"""