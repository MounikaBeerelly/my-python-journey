#! python3

import os
os.system("cls")

import pandas as pd

# Build Series Using list

empnoList = [101, 102, 103, 104, 105, 106, 107, 108, 109]

empnoSeries = pd.Series(empnoList)

print("\nThe employee numbers captured are..", end="\n")
print(empnoSeries)


"""
Output:
------
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
"""