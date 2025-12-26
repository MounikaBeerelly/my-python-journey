#!python3

import os
os.system("cls")

# Using Normal function
def getSimpleInterest(inPrincipleAmount, inInterestRate, inTimePeriod) :
    return ((inPrincipleAmount * inInterestRate * inTimePeriod) / 100)
    
inPrincipleAmount = float(input("\nPlease enter the actual Principle Amount taken for loan: "))
inInterestRate = float(input("\nPlease enter the interest rate applied for this loan: "))
inTimePeriod = float(input("\nPlease enter the time period for this loan: "))

simpleInterest = getSimpleInterest(inPrincipleAmount, inInterestRate, inTimePeriod)

print("\nThe simple interest for an amount of %0.2f, with an interest rate of %0.2f, applied with time period of %0.2f is finally calculated to %0.2f" %(inPrincipleAmount, inInterestRate, inTimePeriod, simpleInterest), end="\n")
print("\nThe final amount to be paid is: %0.2f" %(inPrincipleAmount + simpleInterest), end="\n")

"""
Output:
-------
Please enter the actual Principle Amount taken for loan: 100000

Please enter the interest rate applied for this loan: 2

Please enter the time period for this loan: 12

The simple interest for an amount of 100000.00, with an interest rate of 2.00, applied with time period of 12.00 is finally calculated to 24000.00

The final amount to be paid is: 124000.00

"""

# Using Lambda function
getSimpleInterestLF = lambda inPrincipleAmount, inInterestRate, inTimePeriod : ((inPrincipleAmount * inInterestRate * inTimePeriod) / 100)
    
inPrincipleAmount = float(input("\nPlease enter the actual Principle Amount taken for loan: "))
inInterestRate = float(input("\nPlease enter the interest rate applied for this loan: "))
inTimePeriod = float(input("\nPlease enter the time period for this loan: "))

simpleInterest = getSimpleInterestLF(inPrincipleAmount, inInterestRate, inTimePeriod)

print("\nThe simple interest for an amount of %0.2f, with an interest rate of %0.2f, applied with time period of %0.2f is finally calculated to %0.2f" %(inPrincipleAmount, inInterestRate, inTimePeriod, simpleInterest), end="\n")
print("\nThe final amount to be paid is: %0.2f" %(inPrincipleAmount + simpleInterest), end="\n")

"""
Output:
-------
Please enter the actual Principle Amount taken for loan: 25000

Please enter the interest rate applied for this loan: 2.50

Please enter the time period for this loan: 6

The simple interest for an amount of 25000.00, with an interest rate of 2.50, applied with time period of 6.00 is finally calculated to 3750.00

The final amount to be paid is: 28750.00
"""