import os
os.system("cls")

import pandas as pd
import numpy as np

# build Series Using Numpy array

empnoArray = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109])

empnoSeries = pd.Series(empnoArray)

print("\nThe employee numbers captured are..", end="\n")
print(empnoSeries)

indexValue = int(input("\nPlease enter the index value for the Series to display:"))
print(empnoSeries[ indexValue ])

"""
Output:
=======
The employee numbers captured are..
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

Please enter the index value for the Series to display:3
104

"""