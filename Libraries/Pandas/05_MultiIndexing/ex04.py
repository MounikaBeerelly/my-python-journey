import os
os.system("cls")

import pandas as pd

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")

print("\n", deptDataFrame['DEPTNO'].sum(), end="\n")


"""
Output:
=======
100
"""