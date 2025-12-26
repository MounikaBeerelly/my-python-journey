#!python3

import os
os.system("cls")

def executeGreeting(inObjectName) :
    print(f"\nHello! {inObjectName}", end="\n")
    
    def queryStatus() :
        print(f"\nHow are you feeling today, {inObjectName}", end="\n")
        return
    
    queryStatus()
    return

def main() :
    print("\nInitializing the module to query the status... Please wait", end="\n")
    inName = input("\nPlease enter your name to Query: ")
    executeGreeting(inName)
    return
    
if __name__ == "__main__" :
    main()
    
"""
Output:
-------

Initializing the module to query the status... Please wait

Please enter your name to Query: Akash

Hello! Akash

How are you feeling today, Akash

"""
    