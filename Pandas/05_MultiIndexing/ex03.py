import os
os.system("cls")

import pandas as pd

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")

deptDataAsFrame = pd.MultiIndex.from_frame(deptDataFrame)

print("\n", deptDataAsFrame, end="\n")

#Level 0
level0Data = deptDataAsFrame.get_level_values(0)
#level0Data = deptDataAsFrame.get_level_values('DEPTNO)
print("\n", level0Data, end = "\n")

#Level 1
level1Data = deptDataAsFrame.get_level_values(1)
#level0Data = deptDataAsFrame.get_level_values('DNAME)
print("\n", level1Data, end = "\n")

#Level 2
level2Data = deptDataAsFrame.get_level_values(2)
#level0Data = deptDataAsFrame.get_level_values('LOC)
print("\n", level2Data, end = "\n")

"""
Output:
=======

 MultiIndex([(10, 'ACCOUNTING', 'NEW YORK'),
            (20,   'RESEARCH',   'DALLAS'),
            (30,      'SALES',  'CHICAGO'),
            (40, 'OPERATIONS',   'BOSTON')],
           names=['DEPTNO', 'DNAME', 'LOC'])

 Index([10, 20, 30, 40], dtype='int64', name='DEPTNO')

 Index(['ACCOUNTING', 'RESEARCH', 'SALES', 'OPERATIONS'], dtype='object', name='DNAME')

 Index(['NEW YORK', 'DALLAS', 'CHICAGO', 'BOSTON'], dtype='object', name='LOC')
 """