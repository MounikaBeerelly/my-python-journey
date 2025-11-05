import os
os.system("cls")

import pandas as pd
import numpy as np

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv", index_col = "DEPTNO")
    
print("\nThe data is loaded successfully, redirecting the data to the console...", end="\n")

print("\n", deptDataFrame, end = "\n")

# remove data from dataframe
deptDataFrame.drop([30], inplace = True )

print("\n", deptDataFrame, end="\n")


"""
OUTPUT:
=======

The data is loaded successfully, redirecting the data to the console...

              DNAME       LOC
DEPTNO
10      ACCOUNTING  NEW YORK
20        RESEARCH    DALLAS
30           SALES   CHICAGO
40      OPERATIONS    BOSTON

              DNAME       LOC
DEPTNO
10      ACCOUNTING  NEW YORK
20        RESEARCH    DALLAS
40      OPERATIONS    BOSTON
"""