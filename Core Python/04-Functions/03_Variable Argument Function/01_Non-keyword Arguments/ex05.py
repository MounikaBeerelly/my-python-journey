#!python3

import time

import os
os.system("cls")

def greetingMaker(inGreetMessage, *args) :
   #function to prepare a greeting message in the application
   return f"{inGreetMessage}, " + " ".join(args)

print("\nThe main application begins here...", end="\n")

print(greetingMaker("Hello", "John", "Berkely"), end="\n")
print(greetingMaker("Good Morning", "Smith", "Kumar", "Thakur"), end="\n") 
 
    
"""
Output:
-------

The main application begins here...
Hello, John Berkely
Good Morning, Smith Kumar Thakur

"""