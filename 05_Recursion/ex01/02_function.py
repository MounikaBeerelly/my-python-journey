"""
Scenario:
---------
Write a program to generate a series of natural numbers, where the end user inputs the number of natural numbers

1. The above concept can be implemented using the function based approach as the process is iterative begining for an "Initial state" and termination with a specific range given by the end user
"""
import os
os.system("cls")

def normalSeriesSum(inStartParam, inEndParam) :
    #function to calculate the sum of the series of numbers in a range
    if(inStartParam > inEndParam) :
        return 0
    else :
        finalSeriesSum = 0
        for loopIndex in range(inStartParam, inEndParam + 1) :
            finalSeriesSum += loopIndex
        return finalSeriesSum
    
inStartSeries = int(input("\nPlease enter the initial value from where we should initiate the calculation of the sum of the series :"))
inEndSeries = int(input("\nPlease enter the final value from where we should finalize the calculation of the sum of the series :"))

outFinalSeriesSum = normalSeriesSum(inStartSeries, inEndSeries)


print("\nThe sum of the series from ", inStartSeries, "to ", inEndSeries, "is: ", outFinalSeriesSum, end="\n")

"""
Output:
-------
Please enter the initial value from where we should initiate the calculation of the sum of the series :5

Please enter the final value from where we should finalize the calculation of the sum of the series :10

The sum of the series from  5 to  10 is:  45
"""
