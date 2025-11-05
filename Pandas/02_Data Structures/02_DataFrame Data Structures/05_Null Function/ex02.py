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

print("\n", missingStatus)

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

Please enter the column name on which the missing values should be displayed: MGR

 0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8      True
9     False
10    False
11    False
12    False
13    False
Name: MGR, dtype: bool
"""
