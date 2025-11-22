"""
Scenario:
---------
Write a program to generate a series of natural numbers, where the end user inputs the number of natural numbers

1. The above concept can be implemented using the loop based approach as the process is iterative begining for an "Initial state" and termination with a specific range given by the end user
"""
import os
os.system("cls")

generateValues = int(input("\nPlease enter the number of natural numbers to be generated :"))

print("\nGenerating the natural numbers from 1 to ", generateValues, end="\n")

print()

for seriesIndex in range(1,generateValues + 1) :
    print(seriesIndex, ",", end = "")
    
print()
"""
Output:
-------

Please enter the number of natural numbers to be generated :13

Generating the natural numbers from 1 to  13

1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,

"""