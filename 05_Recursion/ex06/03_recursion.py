import os
import sys
os.system("cls")

def calculateFactorial(inParam) :
    #Function to calculate the sum of series with recursion
    if inParam == 0 :
        return 1
    else:
        return inParam * calculateFactorial(inParam - 1)
        
def seriesSum(inParam) :
    # function to calculate the sum of the given series calling the factorial function at each level      
    seriesTotal = 0.0
    for seriesIndex in range(1, inParam + 1) :
        currentComponentValue = seriesIndex / calculateFactorial(seriesIndex)
        seriesTotal += currentComponentValue
        
        if seriesIndex == 1:
            seriesString = f"{seriesIndex} / {seriesIndex}!"
        else:
            seriesString += " + " + f"{seriesIndex}/{seriesIndex}!"

    return seriesTotal, seriesString
    
seriesLevel = int(input("\nPlease give the final level of the Series: "))

seriesSumValue, seriesStringformat = seriesSum(seriesLevel)

print("The sum of the series in the foramt of \"1/1! + 2/2! + 3/3! + .. + n/n!\"", end="\n")
print(f"\nThe sum of the generated series {seriesStringformat} is : {seriesSumValue}", end = "\n")

"""
Output:
------
Please give the final level of the Series: 7
The sum of the series in the foramt of "1/1! + 2/2! + 3/3! + .. + n/n!"

The sum of the generated series 1 / 1! + 2/2! + 3/3! + 4/4! + 5/5! + 6/6! + 7/7! is : 2.7180555555555554
"""
