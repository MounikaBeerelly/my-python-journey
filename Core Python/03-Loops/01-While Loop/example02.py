"""
Scenario:
---------
Write a program to generate sequence of numbers, where the start range and end range is proposed by the end user
"""

#!python3

import os
os.system("cls")

startRange =  endRange = 0

startRange = int(input("\nPlease enter the starting range value to print the series:"))
endRange = int(input("\nPlease enter the ending range value to terminate the series:"))

print("\nThe sequence of numbers expected to generate are from %d To %d,"%(startRange,endRange), end="\n")

print("\nInitializing the loop for execution.. Please wait..",end="\n")
print("\nPrinting the sequence of numbers from %d To %d,"%(startRange,endRange),"are:",end="\n")

while(startRange <= endRange):
    print("%d"%(startRange),end=" ") 
    startRange = startRange + 1

#Out of the looping process working in the main program
print("\nOut of the iterative process working in the main application space",end="\n")
