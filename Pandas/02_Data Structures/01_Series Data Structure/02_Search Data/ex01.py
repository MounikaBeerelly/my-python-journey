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
    indexPosition = int(input("\nPlease enter the index number of the element to be displayed: "))
    
    if indexPosition >= 0 and indexPosition <= empnoSeries.size :
        print("\nFound the elemnt.. Printing the value..", end="\n")
        print("\nThe employee number found is: ", empnoSeries[indexPosition], end="\n")
        
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

Please enter the index number of the element to be displayed: 2

Found the elemnt.. Printing the value..

The employee number found is:  103

Do you want to search once again (Y OR N) :n

You requested to terminate the Search... Quitting the application..

"""