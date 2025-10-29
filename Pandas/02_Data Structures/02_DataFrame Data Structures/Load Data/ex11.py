import os
os.system("cls")

import pandas as pd
import numpy as np

deptData = [
    {'deptno': 10, 'dname': 'ACCOUNTING', 'deptloc': 'NEW YORK'},
    {'deptno': 20, 'dname': 'RESEARCH', 'deptloc': 'DALLAS'},
    {'deptno': 30, 'dname': 'SALES', 'deptloc': 'CHICAGO'},
    {'deptno': 40, 'dname': 'OPERATIONS', 'deptloc': 'BOSTON'},
]

deptDataFrame = pd.DataFrame(deptData)

print("\nPrinting the departments data frame, loaded from list of dictionaries...", end="\n")

print(deptDataFrame)

"""
Output:
=======
Printing the departments data frame, loaded from list of dictionaries...
   deptno       dname   deptloc
0      10  ACCOUNTING  NEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON
"""