#! python3

import os
os.system("cls")

import pandas as pd
import numpy as np

empnoArray = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109])

empnoSeries = pd.Series(empnoArray)

queryState = True

while queryState :
    os.system("cls")
    print("\nEmployee numbers captured are...", end="\n")
    print(empnoSeries)
    indexPositions = int(input("\nPlease enter the number of the elements to be displayed: "))
    
    if indexPositions >= 0 and indexPositions <= empnoSeries.size :
        displayPosition = input("\nYou want to search the elemtns from Top OR Bottom (T OR B)..")
        if displayPosition == 'T' or displayPosition == 't' :
            print("\nFound the elements.. Printing the values..", end="\n")
            print("\nThe employee numbers found from Top of the Series are... \n\n", str(empnoSeries[:indexPositions]), end="\n")
        else: 
            print("\nFound the elements.. Printing the values..", end="\n")
            print("\nThe employee numbers found from Bottom of the Series are... \n\n", str(empnoSeries[-indexPositions :]), end="\n")   
    else:
        print("\nSearch index is outside the boundary.. Please try once again..", end="\n")
        
    searchChoice = input("\nDo you want to search once again (Y OR N) :")
    if searchChoice == 'N' or searchChoice == 'n' :
        print("\nYou requested to terminate the Search... Quitting the application..", end="\n")
        queryState = False
        
"""
Output:
-------
Employee numbers captured are...
0    101
1    102
2    103
3    104
4    105
5    106
6    107
7    108
8    109
dtype: int64

Please enter the number of the elements to be displayed:3

You want to search the elemtns from Top OR Bottom (T OR B)..B

Found the elements.. Printing the values..

The employee numbers found from Bottom of the Series are...

6    107
7    108
8    109
dtype: int64

"""