import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

print("\nThe data is loaded successfully, and the total number of records loaded are: " + str(empDataFrame.size), end="\n")

getRecordsValue = int(input("\nPlease enter the number of records to be displayed for analysis: "))

if getRecordsValue >= 0 and getRecordsValue <= empDataFrame.size :
    print("\nExtracting the data from the Dataframe.. Please wait..", end="\n")
    empHeadData = empDataFrame.head(getRecordsValue)
    print("\nPrinting the Employees data...", end="\n")
    print(empHeadData)
else:
    print("\nSorry! Index out of the actual boundary.. csnnot proceed", end="\n")

"""
Note:
-----
1. `dataFrameObj.size` actually returns the total size of the Pandas Dataframe, which is the "total number of data points" in the loaded DataFrame, which is the entire size of the plotting area.
"""

"""
Output:
-------
The data is loaded successfully, and the total number of records loaded are: 112

Please enter the number of records to be displayed for analysis: 4

Extracting the data from the Dataframe.. Please wait..

Printing the Employees data...
   EMPNO  ENAME       JOB     MGR   HIREDATE   SAL   COMM  DEPTNO
0   7369  SMITH     CLERK  7902.0  17-Dec-80   800    NaN      20
1   7499  ALLEN  SALESMAN  7698.0  20-Feb-81  1600  300.0      30
2   7521   WARD  SALESMAN  7698.0  22-Feb-81  1250  500.0      30
3   7566  JONES   MANAGER  7839.0   2-Apr-81  2975    NaN      20
"""