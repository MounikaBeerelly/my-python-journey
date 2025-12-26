"""
Scenario:
---------
Write a program to generate the sum of the following series given the number of values: 1/1! + 2/2! + 3/3! + ... + n/n!
"""

import os
import sys
os.system("cls")

seriesLevel = int(input("\nPlease give the final level of the Series: "))

seriesSum = 0.0
factorialValue = 1.0
currentComponentValue = 0.0

for seriesIndex in range(1, seriesLevel + 1) :
    factorialValue *= seriesIndex
    currentComponentValue = seriesIndex / factorialValue
    seriesSum += currentComponentValue
    
    if seriesIndex == 1:
        seriesString = "1/1!"
    else:
        seriesString += " + " + f"{seriesIndex}/{seriesIndex}!"
        
print("The sum of the series in the foramt of \"1/1! + 2/2! + 3/3! + .. + n/n!\"", end="\n")
print(f"\nThe sum of the generated series {seriesString} is : {seriesSum}", end = "\n")
    
"""
Output:
-------

Please give the final level of the Series: 5
The sum of the series in the foramt of "1/1! + 2/2! + 3/3! + .. + n/n!"

The sum of the generated series 1/1! + 2/2! + 3/3! + 4/4! + 5/5! is : 2.708333333333333
"""