import os
os.system("cls")

import pandas as pd

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")

deptDataAsFrame = pd.MultiIndex.from_frame(deptDataFrame)

print("\n", deptDataAsFrame, end="\n")

"""
Output:
=======

 MultiIndex([(10, 'ACCOUNTING', 'NEW YORK'),
            (20,   'RESEARCH',   'DALLAS'),
            (30,      'SALES',  'CHICAGO'),
            (40, 'OPERATIONS',   'BOSTON')],
           names=['DEPTNO', 'DNAME', 'LOC'])

"""