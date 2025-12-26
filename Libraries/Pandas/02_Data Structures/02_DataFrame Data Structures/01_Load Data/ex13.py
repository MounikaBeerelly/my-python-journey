import os
os.system("cls")

import pandas as pd
import numpy as np

# Imbalanced data
deptData = [
    {'deptno': 10, 'dname': 'ACCOUNTING', 'deptloc': 'NEW YORK'},
    {'deptno': 20, 'dname': 'RESEARCH', 'deptloc': 'DALLAS'},
    {'deptno': 30, 'dname': 'SALES', 'deptloc': 'CHICAGO'},
    {'deptno': 40, 'dname': 'OPERATIONS', 'deptloc': 'BOSTON'},
    {'deptno': 40, 'dname': 'SHIPPING'}
]

deptDataFrame = pd.DataFrame(deptData, index = ['Row01', 'Row02', 'Row03','Row04', 'Row05'], columns = ['deptno', 'dname', 'deptloc', 'website'])

print("\nPrinting the departments data frame, loaded from list of dictionaries...", end="\n")

print(deptDataFrame)


"""
Output:
=======


Printing the departments data frame, loaded from list of dictionaries...
       deptno       dname   deptloc  website
Row01      10  ACCOUNTING  NEW YORK      NaN
Row02      20    RESEARCH    DALLAS      NaN
Row03      30       SALES   CHICAGO      NaN
Row04      40  OPERATIONS    BOSTON      NaN
Row05      40    SHIPPING       NaN      NaN

"""