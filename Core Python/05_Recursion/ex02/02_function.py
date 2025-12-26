"""
Scenario:
---------
Write a program to generate a series of natural numbers, where the end user inputs the number of natural numbers

1. The above concept can be implemented using the function based approach as the process is iterative begining for an "Initial state" and termination with a specific range given by the end user
"""
import os
os.system("cls")

def generateSeries(inParam) :
    #function to generate the natural number series for a given range
    print()
    
    for seriesIndex in range(1, inParam + 1) :
        print(seriesIndex, end="\n")
        
    print()
    return
    
generateValues = int(input("\nPlease enter the number of natural numbers to be generated :"))

print("\nGenerating the NAtural numbers from 1 to ", generateValues, end="\n")

"""
Output:
-------
Please enter the number of natural numbers to be generated :6

Generating the NAtural numbers from 1 to  6
1
2
3
4
5
6
"""
