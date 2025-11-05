import os
os.system("cls")

import pandas as pd
import numpy as np

empSearchList = []

columnIndex = 1

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

for columnLabels in empDataFrame.columns :
    print(str(columnIndex) + ". " + columnLabels)
    columnIndex += 1
    
columnLabelList = list(empDataFrame.columns)

statusColumn = input("\nPlease enter the column name on which the missing values should be displayed: ")

missingStatus = pd.isnull(empDataFrame[statusColumn])

print("\n", empDataFrame[missingStatus])

"""
Output:
-------
1. EMPNO
2. ENAME
3. JOB
4. MGR
5. HIREDATE
6. SAL
7. COMM
8. DEPTNO

Please enter the column name on which the missing values should be displayed: COMM

     EMPNO   ENAME        JOB     MGR   HIREDATE   SAL  COMM  DEPTNO
0    7369   SMITH      CLERK  7902.0  17-Dec-80   800   NaN      20
3    7566   JONES    MANAGER  7839.0   2-Apr-81  2975   NaN      20
5    7698   BLAKE    MANAGER  7839.0   1-May-81  2850   NaN      30
6    7782   CLARK    MANAGER  7839.0   9-Jun-81  2450   NaN      10
7    7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000   NaN      20
8    7839    KING  PRESIDENT     NaN  17-Nov-81  5000   NaN      10
10   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100   NaN      20
11   7900   JAMES      CLERK  7698.0   3-Dec-81   950   NaN      30
12   7902    FORD    ANALYST  7566.0   3-Dec-81  3000   NaN      20
13   7934  MILLER      CLERK  7782.0  23-Jan-82  1300   NaN      10
"""
