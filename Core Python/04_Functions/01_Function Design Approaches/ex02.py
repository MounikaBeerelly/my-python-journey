#!python3

import time
import os

# All the user defined functions definitions go here

def functionOne():
    #The functionOne definition goes here
    print("\nHai! Greetings from \"functionOne()\", called from the main module scope", end="\n")
    tempState = input()
    print("\nNow leaving the \"functionOne()\", and returning to the main block scope from where it is called",end="\n")
    tempState = input()
    return

def functionTwo():
    #The functionTwo definition goes here
    print("\nHai! Greetings from \"functionTwo()\", called from the main module scope", end="\n")
    tempState = input()
    print("\nNow leaving the \"functionTwo()\", and returning to the main block scope from where it is called",end="\n")
    tempState = input()
    return

def functionThree():
    #The functionThree definition goes here
    print("\nHai! Greetings from \"functionThree()\", called from the main module scope", end="\n")
    tempState = input()
    print("\nNow leaving the \"functionThree()\", and returning to the main block scope from where it is called",end="\n")
    tempState = input()
    return

#All the main block operations goes here

os.system("cls")

print("\nMain block of python application has started...", end="\n")
time.sleep(3)
print("\nCalling the function \"functionOne()\" from the main blovk of the python code", end="\n")
functionOne()
time.sleep(3)
print("\nReturn from the function \"functionOne()\" operating in the main blovk of the python code, About to call \"functionTwo()\"", end="\n")
time.sleep(3)

print("\nCalling the function \"functionTwo()\" from the main blovk of the python code", end="\n")
functionTwo()
time.sleep(3)
print("\nReturn from the function \"functionTwo()\" operating in the main blovk of the python code, About to call \"functionThree()\"", end="\n")
time.sleep(3)

print("\nCalling the function \"functionThree()\" from the main blovk of the python code", end="\n")
functionThree()
time.sleep(3)
print("\nReturn from the function \"functionThree()\" operating in the main blovk of the python code, About to return to the next level of operations in main thread", end="\n")
time.sleep(3)

print("\nFinally returned to the main block of the program.. Moving towards termination...",end="\n")
print("\nNow leaving the main block of the python application closing the application level scope...",end="\n")
time.sleep(3)

#All the main blok operations will terminate here