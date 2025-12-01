#!python3

import os
os.system("cls")

def getGreetings() :
    print("\nHello! This message is from Greeting function", end="\n")
    return
    
if __name__ == "__main__" :
    print("\nOperating in the global scope of the application..", end="\n")
    print("\nThe Reference address to the function is: ", getGreetings, end="\n")
    getGreetings()
    
"""
Output:
-------
Operating in the global scope of the application..

The Reference address to the function is:  <function getGreetings at 0x0000025579DCE040>

Hello! This message is from Greeting function

"""
    