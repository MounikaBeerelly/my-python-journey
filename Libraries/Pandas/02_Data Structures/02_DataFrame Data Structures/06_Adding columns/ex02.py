import os
os.system("cls")

import pandas as pd
import numpy as np

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")
    
print("\nThe data is loaded successfully, redirecting the data to the console...", end="\n")

print("\n", deptDataFrame, end = "\n")

# values to be adding to the dataframe
deptState = ["Financial Head Quarteres", "Think Tank Center", "Market Analysis Center", "Administrative Head Quarters"]

# add the column to the dataframe with position
deptDataFrame.insert(2, "DEPTSTATE", deptState, True)

print("\n", deptDataFrame, end="\n")

"""
OUTPUT:
=======
The data is loaded successfully, redirecting the data to the console...

    DEPTNO       DNAME       LOC
0      10  ACCOUNTING  NEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON

    DEPTNO       DNAME                     DEPTSTATE       LOC
0      10  ACCOUNTING      Financial Head Quarteres  NEW YORK
1      20    RESEARCH             Think Tank Center    DALLAS
2      30       SALES        Market Analysis Center   CHICAGO
3      40  OPERATIONS  Administrative Head Quarters    BOSTON

"""