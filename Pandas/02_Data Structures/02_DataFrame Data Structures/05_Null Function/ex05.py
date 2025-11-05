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

missingStatus = pd.notnull(empDataFrame[statusColumn])

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

    EMPNO   ENAME       JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
1   7499   ALLEN  SALESMAN  7698.0  20-Feb-81  1600   300.0      30
2   7521    WARD  SALESMAN  7698.0  22-Feb-81  1250   500.0      30
4   7654  MARTIN  SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
9   7844  TURNER  SALESMAN  7698.0   8-Sep-81  1500     0.0      30
"""
