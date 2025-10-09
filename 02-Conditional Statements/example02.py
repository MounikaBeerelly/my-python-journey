"""
Scenario:
---------
1. Write a program that takes the input of the Baggage weight from the end user.
2. The program should also accept the "Unit od Measure" either as "Kilograms" OR "Ponds".
3. Taking the given unit it has to calculate whether the baggage is acceptable to standard baggage weight as per the flight standards.
    i. Consider the default acceptable weight is 23 Kgs.
4. If the given baggage is within the acceptable limits, give a valid message to the end user, accepting the baggage.
5. If the given baggage is not within the acceptable limits
    a. Display the extra weight
    b. Calculate the additional charges to be paid by the passenger considering "500" as the multiple value upon the excess weight.
"""

#!python3

import os
os.system("cls")

print("\nPlease choose the unit of measure")
print("--------------------------")
print("\n1.Kilograms", end="\n")
print("\n2.Pounds", end="\n")

unitMeasure = int(input("\nPlease enter your choice of the unit :"))
baggageWeight = float(input("\n\nPlease enter the weight of your suitcase: "))

if(unitMeasure != 1):
    baggageWeight *= 0.4535923

print("\nThe default weight allowed free of charges in the flight is: 23Kgs", end="\n")
print("\nYour given baggage weight is: %.2f"%(baggageWeight),"Kgs.", end="\n")

if(baggageWeight>23):
    print("\nAlert baggage weight is more than the accepted limit", end="\n")
    extraWeight = baggageWeight - 23
    print("\nExtra weight identified is: %2f"%(extraWeight),"Kgs",end="\n")
    print("\nThe excess amount to be paid for the extra baggage is %.2f" %(extraWeight*500), "INR", end="\n")
else:
    print("\nYour baggage is accepted..",end="\n")
    print("\nPlease place on the conveyor belt",end="\n")
    print("\nHappy journey! Thank you for travelling with us.", end="\n")