"""
Scenario:
---------
Write a program to generate a series of sequential numbers in a specified range, to calculate the final sum

1. The above concept can be implemented using the function based approach as the process is iterative begining for an "Initial state" and termination with a specific range given by the end user
"""
import os
os.system("cls")

def recursiveSeriesSum(inStartParam, inEndParam) :
    #function to calculate the sum of the series of numbers in a range using Recursion
    if(inStartParam > inEndParam) :
        return 0
    else :
        nextValue = inStartParam + 1
        currentSum = recursiveSeriesSum(nextValue, inEndParam)
        recursiveFinalSum = inStartParam + currentSum
        return recursiveFinalSum
    
inStartSeries = int(input("\nPlease enter the initial value from where we should initiate the calculation of the sum of the series :"))
inEndSeries = int(input("\nPlease enter the final value from where we should finalize the calculation of the sum of the series :"))

outFinalSeriesSum = recursiveSeriesSum(inStartSeries, inEndSeries)

print("\nThe sum of the series from ", inStartSeries, "to ", inEndSeries, "is: ", outFinalSeriesSum, end="\n")

"""
Output:
-------

Please enter the initial value from where we should initiate the calculation of the sum of the series :5

Please enter the final value from where we should finalize the calculation of the sum of the series :10

The sum of the series from  5 to  10 is:  45

"""