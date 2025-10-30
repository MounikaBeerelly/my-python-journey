import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv", index_col="EMPNO")

print("\nThe data is loaded successfully, Redirecting the data to the console...", end="\n")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(empDataFrame)

searchValue = int(input("\nPlease enter the Employee Number to retrieve the record: "))

empRecord = empDataFrame.loc[searchValue]

print("\nThe Details of the employee with Employee number: " + str(searchValue) + " are..", end="\n")
print(empRecord)

"""
Output:
=======
The data is loaded successfully, Redirecting the data to the console...
        ENAME        JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
EMPNO
7369    SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20
7499    ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30
7521     WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30
7566    JONES    MANAGER  7839.0   2-Apr-81  2975     NaN      20
7654   MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
7698    BLAKE    MANAGER  7839.0   1-May-81  2850     NaN      30
7782    CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN      10
7788    SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN      20
7839     KING  PRESIDENT     NaN  17-Nov-81  5000     NaN      10
7844   TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0      30
7876    ADAMS      CLERK  7788.0  12-Jan-83  1100     NaN      20
7900    JAMES      CLERK  7698.0   3-Dec-81   950     NaN      30
7902     FORD    ANALYST  7566.0   3-Dec-81  3000     NaN      20
7934   MILLER      CLERK  7782.0  23-Jan-82  1300     NaN      10

Please enter the Employee Number to retrieve the record: 7844

The Details of the employee with Employee number: 7844 are..
ENAME         TURNER
JOB         SALESMAN
MGR           7698.0
HIREDATE    8-Sep-81
SAL             1500
COMM             0.0
DEPTNO            30
Name: 7844, dtype: object

"""