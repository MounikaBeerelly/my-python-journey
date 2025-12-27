#!python3

import os
os.system("cls")

def greetUser(**kwargs) :
    greetMessage = kwargs.get("greetMessage", "Hello")
    userName = kwargs.get("userName", "There")
    greetPunctuation = kwargs.get("greetPunctuation", "!")
    
    print(f"{greetMessage}, {userName}{greetPunctuation}", end="\n")
    
print("\nThis is the main module..", end="\n")
print("---------------------------", end="\n")

greetUser(greetMessage = "Hai", userName = "Abdul")
greetUser(userName = "Akshay", greetPunctuation = "...")
greetUser(greetMessage = "Good Morning", userName = "Kumar")

"""
Output :
=======
This is the main module..
---------------------------
Hai, Abdul!
Hello, Akshay...
Good Morning, Kumar!
"""