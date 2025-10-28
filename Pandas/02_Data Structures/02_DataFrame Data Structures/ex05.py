import os
os.system("cls")

import pandas as pd
import numpy as np

empData = [
    [7369,'SMITH','CLERK',7902,'17-NOV-81',800,np.nan,20],
    [7499,'ALLEN','SALESMAN',7698,'21-JAN-81',1600,300,30],
    [7521,'WARD','SALESMAN',7698,'02-AUG-81',1250,500,30],
    [7566,'JONES','MANAGER',7839,'09-SEP-81',2975,np.nan,20],
    [7654,'MARTIN','SALESMAN',7698,'13-NOV-83',1250,1400,30],
    [7698,'BLAKE','MANAGER',7839,'11-FEB-82',2850,np.nan,30,],
    [7782,'CLARK','MANAGER',7839,'23-MAR-81',2450,np.nan,10],
    [7788,'SCOTT','ANALYST',7566,'30-JUN-81',3000,np.nan,20],
    [7839,'KING','PRESIDENT',np.nan,'01-MAY-81',5000,np.nan,10],
    [7844,'TURNER','SALESMAN',7698,'09-DEC-82',1500,0,30],
    [7876,'ADAMS','CLERK',7788,'23-JUL-81',1100,np.nan,20],
    [7900,'JAMES','CLERK',7698,'17-DEC-80',950,np.nan,30],
    [7902,'FORD','ANALYST',7566,'22-FEB-81',3000,np.nan,20],
    [7934,'MILLER','CLERK',7782,'19-NOV-81',1300,np.nan,10]
]
empDataFrame = pd.DataFrame(empData, columns=['Empno', 'EmpName', 'EmpJob', 'EmpMgr', 'EmpHireDate', 'EmpSal', 'EmpComm', 'EmpDeptID'])

print(f"\nPrinting the employees data frame, loaded with employee data as a columns..", end="\n")

print("\nPrinting the employees Data frame, loaded with the applied labels for each Series and missing values as NaN..", end="\n")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(empDataFrame)


"""
Output:
-------

Printing the employees data frame, loaded with employee data as a columns..

Printing the employees Data frame, loaded with the applied labels for each Series and missing values as NaN..
    Empno EmpName     EmpJob  EmpMgr EmpHireDate  EmpSal  EmpComm  EmpDeptID
0    7369   SMITH      CLERK  7902.0   17-NOV-81     800      NaN         20
1    7499   ALLEN   SALESMAN  7698.0   21-JAN-81    1600    300.0         30
2    7521    WARD   SALESMAN  7698.0   02-AUG-81    1250    500.0         30
3    7566   JONES    MANAGER  7839.0   09-SEP-81    2975      NaN         20
4    7654  MARTIN   SALESMAN  7698.0   13-NOV-83    1250   1400.0         30
5    7698   BLAKE    MANAGER  7839.0   11-FEB-82    2850      NaN         30
6    7782   CLARK    MANAGER  7839.0   23-MAR-81    2450      NaN         10
7    7788   SCOTT    ANALYST  7566.0   30-JUN-81    3000      NaN         20
8    7839    KING  PRESIDENT     NaN   01-MAY-81    5000      NaN         10
9    7844  TURNER   SALESMAN  7698.0   09-DEC-82    1500      0.0         30
10   7876   ADAMS      CLERK  7788.0   23-JUL-81    1100      NaN         20
11   7900   JAMES      CLERK  7698.0   17-DEC-80     950      NaN         30
12   7902    FORD    ANALYST  7566.0   22-FEB-81    3000      NaN         20
13   7934  MILLER      CLERK  7782.0   19-NOV-81    1300      NaN         10

"""