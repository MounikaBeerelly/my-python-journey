#!python3

import time
import os
os.system("cls")

# without Decorators
def slowFunction() :
    time.sleep(2)
    return "done with the task!"

def timeTracker(infunctionName) :
    startTime = time.time()
    finalResult = infunctionName()
    endTime = time.time()
    print(f"\nThe total execution time is : {endTime - startTime} seconds", end="\n")
    return finalResult

if __name__ == "__main__" :
    print("\n------- Without Decorators ---------------", end="\n")
    print(f"The time consumed by the function is : {timeTracker(slowFunction)}", end="\n")
    
# with Decorators

def timeTracker(infunctionName) :
    def wrapperFunction() :
        startTime = time.time()
        finalResult = infunctionName()
        endTime = time.time()
        print(f"\nThe total execution time is : {endTime - startTime} seconds", end="\n")
        return finalResult
    return wrapperFunction

@timeTracker
def slowFunction() :
    time.sleep(2)
    return "done with the task!"

if __name__ == "__main__" :
    print("\n------- With Decorators ---------------", end="\n")
    print(f"The time consumed by the function is : {slowFunction()}", end="\n")
    

"""
Output:
-------

------- Without Decorators ---------------

The total execution time is : 2.007037878036499 seconds
The time consumed by the function is : done with the task!

------- With Decorators ---------------

The total execution time is : 2.0091054439544678 seconds
The time consumed by the function is : done with the task!

"""