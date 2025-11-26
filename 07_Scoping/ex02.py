#!python3

import os
os.system("cls")

def outerFunction() :
    print("\nThis message is from outer function scope", end="\n")
    def innerFunction() :
        print("\nThis message is from Inner function scope", end="\n")
        return 
    
    innerFunction()
    return

def main() :
    print("\nWorking under the scope of the user defined \"main()\" function", end="\n")
    outerFunction()
    return

if __name__ == "__main__": # PSP - Program Starting Point
    print("\nOperating in the Global scope of the application...", end="\n")
    main()
    
    
"""
Output:
-------
Operating in the Global scope of the application...

Working under the scope of the user defined "main()" function

This message is from outer function scope

This message is from Inner function scope
"""