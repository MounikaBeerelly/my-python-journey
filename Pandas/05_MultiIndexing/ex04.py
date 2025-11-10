import os
os.system("cls")

import pandas as pd

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")

print("\n", deptDataFrame.sum(), end="\n")

deptDataAsFrame = pd.MultiIndex.from_frame(deptDataFrame)

print("\n", deptDataAsFrame, end="\n")



"""
Output:
=======

"""