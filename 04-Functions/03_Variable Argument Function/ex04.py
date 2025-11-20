#!python3

import time

import os
os.system("cls")

def printArguments(*args) :
   #function to print the given parameters passed to the function
   print("\nThe given parameters from the end user are: ", args, end="\n")
   for outIndex, outArgument in enumerate(args, start = 1) :
       print(str(outIndex) + "." + str(outArgument))
   return

print("\nThe main application begins here...", end="\n")

print("\nThe given words are \"Hello\", \"World\"")
printArguments("Hello", "World")

print("\nThe given personal information is: \"John\", \"Berkley\", \"40\", \"80.55\", \"8023456123\", \"John@gmail.com\" ")
printArguments("John", "Berkley", 40, 80.55, 8023456123, "John@gmail.com")
 
    
"""
Output:
-------

The main application begins here...

The given words are "Hello", "World"

The given parameters from the end user are:  ('Hello', 'World')
1.Hello
2.World

The given personal information is: "John", "Berkley", "40", "80.55", "8023456123", "John@gmail.com"

The given parameters from the end user are:  ('John', 'Berkley', 40, 80.55, 8023456123, 'John@gmail.com')
1.John
2.Berkley
3.40
4.80.55
5.8023456123
6.John@gmail.com
"""