"""
Scenario 02
===========
Write a program that takes from the end user till the end user terminates by typing "quit" else find square
"""
#!python3

import os
import time
os.system("cls")

loopState = False

while not loopState: 
    inputVal = input("\nPlease enter a number for calculating the square (type 'exit' to quit):")
    
    if inputVal.lower() == "exit":
        loopState = True
    else:
        inputVal = int(inputVal)
        print("\nThe square of the given number %d is: %d"%(inputVal, (inputVal**2)),end="\n")