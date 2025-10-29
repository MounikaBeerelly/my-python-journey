import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

empTailData = empDataFrame.tail()

print("\nPrinting the Employees data...", end="\n")
print(empTailData)

"""
Output:
======
Printing the Employees data...
    EMPNO   ENAME       JOB     MGR   HIREDATE   SAL  COMM  DEPTNO
9    7844  TURNER  SALESMAN  7698.0   8-Sep-81  1500   0.0      30
10   7876   ADAMS     CLERK  7788.0  12-Jan-83  1100   NaN      20
11   7900   JAMES     CLERK  7698.0   3-Dec-81   950   NaN      30
12   7902    FORD   ANALYST  7566.0   3-Dec-81  3000   NaN      20
13   7934  MILLER     CLERK  7782.0  23-Jan-82  1300   NaN      10
"""
