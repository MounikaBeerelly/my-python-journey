#!python3

"""
Domain : Logistics
Scenario: Calculate shipping cost based on weight and distance
"""

import os
os.system("cls")

from functools import partial

def calculateShipping(inWeight, inDistance, inRatePerKGPerKM) :
    return inWeight * inDistance * inRatePerKGPerKM

if __name__ == "__main__" :
    print("\nCalculating the final price after applying the possible discount", end="\n")
    
    domesticShipping = partial(calculateShipping, inRatePerKGPerKM = 0.05)
    internationalShipping = partial(calculateShipping, inRatePerKGPerKM = 0.10)

    inWeight = float(input("\nPlease enter the original weight of the package (in KG's): "))
    inDistance = int(input("\nPlease enter the distance in KM's : "))
    inShippingType = input("\nPlease enter the shipping type (D: Domestic, I: International) :").lower()
    
    if inShippingType == 'd' :
        print(f"\nThe final domestic shipping cost is : {domesticShipping(inWeight = inWeight, inDistance = inDistance)}", end = "\n")
    elif inShippingType == "i" :
        print(f"\nThe final international shipping cost is : {internationalShipping(inWeight = inWeight, inDistance = inDistance)}", end = "\n")
    else:
        print("\nSorry, invalid shipping type. Please try once again..", end="\n")
    
"""
Output:
------

Calculating the final price after applying the possible discount

Please enter the original weight of the package (in KG's): 100

Please enter the distance in KM's : 20

Please enter the shipping type (D: Domestic, I: International) :d

The final domestic shipping cost is : 100.0
"""