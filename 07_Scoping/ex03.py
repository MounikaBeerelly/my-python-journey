#!python3

import time
import os
os.system("cls")

def outerFunction() :
    print("\nThis message is from outer function scope", end="\n")
    time.sleep(2)
    def innerFunction() :
        print("\nThis message is from inner function scope", end="\n")
        return
    
    innerFunction()
    return

def main() :
    print("\nWorking under the scope of the user defined \"main()\" function", end="\n")
    time.sleep(2)
    outerFunction()
    
if __name__ == "__main__" :
    print("\nOperating in the global scope of the application..", end="\n")
    time.sleep(2)
    main()
    
"""
Output:
-------
Operating in the global scope of the application..

Working under the scope of the user defined "main()" function

This message is from outer function scope

This message is from inner function scope
"""
    