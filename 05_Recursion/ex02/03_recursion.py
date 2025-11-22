"""
Scenario:
---------
Write a program to generate a series of natural numbers, where the end user inputs the number of natural numbers

1. The above concept can be implemented using the function based approach as the process is iterative begining for an "Initial state" and termination with a specific range given by the end user
"""
import os
os.system("cls")

def generateSeries(inParam) :
    #function to generate the natural number series for a given range using recursion
    
    if (inParam > 1) :
        generateSeries(inParam - 1)
        print(inParam, ",", end="\n")
    else:
        print(inParam, ",", end="\n")
    return

generateValues = int(input("\nPlease enter the number of natural numbers to be generated :"))

print("\nGenerating the Natural numbers from 1 to ", generateValues, end="\n")

print()
generateSeries(generateValues)
print()

"""
Output:
-------

Please enter the number of natural numbers to be generated :5

Generating the Natural numbers from 1 to  5

1 ,
2 ,
3 ,
4 ,
5 ,

"""