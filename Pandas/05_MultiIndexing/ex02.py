import os
os.system("cls")

import pandas as pd

deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")

deptDataAsFrame01 = pd.MultiIndex.from_frame(deptDataFrame)

print("\n", deptDataAsFrame01, end="\n")

# with index
deptDataAsFrame02 = pd.MultiIndex.to_frame(deptDataAsFrame01)

print("\n", deptDataAsFrame02, end = "\n")

# without index
deptDataAsFrame03 = pd.MultiIndex.to_frame(deptDataAsFrame01, index = False)

print("\n", deptDataAsFrame03, end = "\n")
"""
Output:
=======
 MultiIndex([(10, 'ACCOUNTING', 'NEW YORK'),
            (20,   'RESEARCH',   'DALLAS'),
            (30,      'SALES',  'CHICAGO'),
            (40, 'OPERATIONS',   'BOSTON')],
           names=['DEPTNO', 'DNAME', 'LOC'])

                             DEPTNO       DNAME       LOC
DEPTNO DNAME      LOC
10     ACCOUNTING NEW YORK      10  ACCOUNTING  NEW YORK
20     RESEARCH   DALLAS        20    RESEARCH    DALLAS
30     SALES      CHICAGO       30       SALES   CHICAGO
40     OPERATIONS BOSTON        40  OPERATIONS    BOSTON

    DEPTNO       DNAME       LOC
0      10  ACCOUNTING  NEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON
"""