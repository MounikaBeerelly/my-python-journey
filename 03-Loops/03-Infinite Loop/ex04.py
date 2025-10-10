"""
Scenario
========
1. Write a program to calculate the final capital amount, given the principal amount, along with the rate of interest and number of years of loan
2. the program should print the capital amount for every of loan period
"""

#!python3

import os
os.system("cls")

inPrincipleAmount = float(input("\nPlease enter the principle amount taken for loan:"))
inRateOfInterest = float(input("\nPlease enter the rate of interest that is applied:"))
inNumberOfYears = float(input("\nPlease enter the number of years to calculate the capital accumulated:"))

inYearIndex = 0

while(inYearIndex < inNumberOfYears):
    inPrincipleAmount += inPrincipleAmount * inRateOfInterest / 100.00
    inYearIndex += 1
    print("\nThe capital amount for year %d is: %0.2f"%(inYearIndex,inPrincipleAmount),end="\n")
else:
    print("\nThe final capital amount accumulated after %d years is:%0.2f"%(inYearIndex,inPrincipleAmount),end="\n")