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
    tailValue = int(input("\nPlease enter the number of the elements to be displayed from bottom: "))
    
    if tailValue <= empnoSeries.size :
       print("\nFound the elements.. Printing the values..", end="\n")
       print("\nThe employee numbers found are... \n\n", str(empnoSeries.tail(tailValue)), end="\n")
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

Please enter the number of the elements to be displayed from bottom: 4

Found the elements.. Printing the values..

The employee numbers found are...

 5    106
6    107
7    108
8    109
dtype: int64

Do you want to search once again (Y OR N) :N

You requested to terminate the Search... Quitting the application..

"""