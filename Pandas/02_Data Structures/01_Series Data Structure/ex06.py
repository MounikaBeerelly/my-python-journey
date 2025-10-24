import os
os.system("cls")

import pandas as pd
import numpy as np

inTestVal = int(input("\nPlease enter the value for the number of test values to be generated: "))

loopState = True

while loopState:
    myTestDataArray = np.random.randn(inTestVal)
    print("\nThe test data filled in a 2 dimensional array is..", end="\n")
    print(myTestDataArray)
    dataSeries = pd.Series(myTestDataArray)
    print("\nThe series of random test data generated for randomly " + str(inTestVal)+ " values is.. ", end="\n")
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


Please enter the value for the number of test values to be generated: 5

The test data filled in a 2 dimensional array is..
[ 0.86422969 -0.30434404  0.92171873 -0.70872706 -0.58665289]

The series of random test data generated for randomly 5 values is..
0    0.864230
1   -0.304344
2    0.921719
3   -0.708727
4   -0.586653
dtype: float64

Do you want to generate another series for testing (Y or N):y

You requested for the application termination...
"""