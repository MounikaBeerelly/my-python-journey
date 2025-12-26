import os
os.system("cls")

import pandas as pd
import numpy as np

# build Series Using Numpy array

empnoArray = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109])

empnoSeries = pd.Series(empnoArray)

print("\nThe employee numbers captured are..", end="\n")
print(empnoSeries)

beginSliceValue = int(input("\nPlease enter the slice value for the Series to display from the beginning of the series:"))
endSliceValue = int(input("\nPlease enter the slice value for the Series to display from the ending of the series:"))
print(empnoSeries[ beginSliceValue : endSliceValue : ])

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

Please enter the slice value for the Series to display from the beginning of the series:4

Please enter the slice value for the Series to display from the ending of the series:7
4    105
5    106
6    107
dtype: int64

"""