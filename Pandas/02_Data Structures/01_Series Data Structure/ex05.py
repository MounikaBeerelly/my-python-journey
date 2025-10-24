import os
os.system("cls")

import pandas as pd
import numpy as np

inStartingVal = int(input("\nPlease enter the starting range of the series to be genereated: "))
inEndingVal = int(input("\nPlease enter the ending range of the series to be genereated: "))

loopState = True

while loopState:
    inStepValue = int(input("\nPlease enter the step value to be applied in the Series: "))

    dataSeries = pd.Series(np.linspace(inStartingVal, inEndingVal, inStepValue))
    print("\nThe series of test data generated from " + str(inStartingVal)+ " To " + str(inEndingVal) + " with step of " + str(inStepValue) + "is..", end="\n")
    print(dataSeries)
    inChoice = input("\nDo you want to generate another series for testing (Y or N):")
    if (inChoice != 'Y' or inChoice != 'y'):
            print("\nYou requested for the application termination...", end="\n")
            loopState = False
    else:
        print("\nGetting ready to generate another test series.. Please wait, emd=\n")
        
"""
Output:
-------

Please enter the starting range of the series to be genereated: 5

Please enter the ending range of the series to be genereated: 20

Please enter the step value to be applied in the Series:5

The series of test data generated from 5 To 20 with step of 5is..
0     5.00
1     8.75
2    12.50
3    16.25
4    20.00
dtype: float64

Do you want to generate another series for testing (Y or N):n

You requested for the application termination...

"""