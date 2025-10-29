#! python3

import os
os.system("cls")

import pandas as pd

# Scalar Series

scalarDataSeries = pd.Series(25, index=[1,2,3,4,5])

print(f"\nThe Scalar Series is..", end="\n")
print(scalarDataSeries)

"""
Output:
------

The Scalar Series is..
1    25
2    25
3    25
4    25
5    25
dtype: int64

"""