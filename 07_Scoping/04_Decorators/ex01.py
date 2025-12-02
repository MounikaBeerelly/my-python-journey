#!python3

import os
os.system("cls")

# without Decorators
def greetFunction(inName) :
    return f"Hello, {inName}!"

def greetingWithExclamation(inName) :
    finalGreeting = greetFunction(inName)
    return f"{finalGreeting}!!!"

if __name__ == "__main__" :
    print("\n------- Without Decorators ---------------", end="\n")
    inName = input("\nPlease enter your name : ")
    print(greetingWithExclamation(inName), end="\n")
    
# with Decorators
def formatExclamation(inFunctionName) :
    def greetingWithExclamation(inName) :
        finalGreeting = inFunctionName(inName)
        return f"{finalGreeting}!!!"
    return greetingWithExclamation

@formatExclamation
def greetFunction(inName) :
    return f"Hello, {inName}!"

if __name__ == "__main__" :
    print("\n------- With Decorators ---------------", end="\n")
    inName = input("\nPlease enter your name : ")
    print(greetFunction(inName), end="\n")
    
    
"""
Output:
-------
------ Without Decorators ---------------

Please enter your name : John
Hello, John!!!!

------- With Decorators ---------------

Please enter your name : Akshay
Hello, Akshay!!!!
"""