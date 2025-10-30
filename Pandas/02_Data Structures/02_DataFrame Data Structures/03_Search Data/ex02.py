import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv", index_col="DEPTNO")

print("\nThe data is loaded successfully, Redirecting the data to the console...", end="\n")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(empDataFrame)

searchValue = int(input("\nPlease enter the Department Number to retrieve the records: "))

empRecord = empDataFrame.loc[searchValue]

print("\nThe Details of the employees with Department number: " + str(searchValue) + " are..", end="\n")
print(empRecord)


"""
Output:
-------

The data is loaded successfully, Redirecting the data to the console...
        EMPNO   ENAME        JOB     MGR   HIREDATE   SAL    COMM
DEPTNO
20       7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN
30       7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0
30       7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0
20       7566   JONES    MANAGER  7839.0   2-Apr-81  2975     NaN
30       7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0
30       7698   BLAKE    MANAGER  7839.0   1-May-81  2850     NaN
10       7782   CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN
20       7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN
10       7839    KING  PRESIDENT     NaN  17-Nov-81  5000     NaN
30       7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0
20       7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     NaN
30       7900   JAMES      CLERK  7698.0   3-Dec-81   950     NaN
20       7902    FORD    ANALYST  7566.0   3-Dec-81  3000     NaN
10       7934  MILLER      CLERK  7782.0  23-Jan-82  1300     NaN

Please enter the Department Number to retrieve the records: 20

The Details of the employees with Department number: 20 are..
        EMPNO  ENAME      JOB     MGR   HIREDATE   SAL  COMM
DEPTNO
20       7369  SMITH    CLERK  7902.0  17-Dec-80   800   NaN
20       7566  JONES  MANAGER  7839.0   2-Apr-81  2975   NaN
20       7788  SCOTT  ANALYST  7566.0   9-Dec-82  3000   NaN
20       7876  ADAMS    CLERK  7788.0  12-Jan-83  1100   NaN
20       7902   FORD  ANALYST  7566.0   3-Dec-81  3000   NaN

"""