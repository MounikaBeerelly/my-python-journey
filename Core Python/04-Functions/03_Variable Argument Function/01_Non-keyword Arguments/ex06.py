#!python3

import time

import os
os.system("cls")

def printInformation(inName, inAge, *args) :
   #function to prepare and print information of the given object
   print(f"Students Name: {inName}, Age: {inAge}")
   for outIndex, outArgument in enumerate(args, start = 1) :
       print(str(outIndex) + ". " +str(outArgument))

print("\nThe main application begins here...", end="\n")

printInformation("John Doe", 35, "Programmer", "Player", "Singer", "Dancer")

printInformation("Ekantha Sai Sundar", 21, "AI and ML Enthusiast", "Book reading", "Likes algorithms and analysis", "Work in IOT") 
 
    
"""
Output:
-------
The main application begins here...
Students Name: John Doe, Age: 35
1. Programmer
2. Player
3. Singer
4. Dancer
Students Name: Ekantha Sai Sundar, Age: 21
1. AI and ML Enthusiast
2. Book reading
3. Likes algorithms and analysis
4. Work in IOT

"""