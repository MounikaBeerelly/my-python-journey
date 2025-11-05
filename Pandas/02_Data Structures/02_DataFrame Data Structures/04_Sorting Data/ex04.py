import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
    
print("\nThe data is loaded successfully, redirecting the data to the console...", end="\n")

print(empDataFrame, end = "\n")

# department no with Salary wise sorting
empDataFrame.sort_values(["DEPTNO", "SAL"], axis = 0, ascending = True, inplace = True, na_position = 'last')

print("\n", empDataFrame, end = "\n")

"""
Output:
-------

The data is loaded successfully, redirecting the data to the console...
    EMPNO   ENAME        JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
0    7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20
1    7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30
2    7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30
3    7566   JONES    MANAGER  7839.0   2-Apr-81  2975     NaN      20
4    7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
5    7698   BLAKE    MANAGER  7839.0   1-May-81  2850     NaN      30
6    7782   CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN      10
7    7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN      20
8    7839    KING  PRESIDENT     NaN  17-Nov-81  5000     NaN      10
9    7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0      30
10   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     NaN      20
11   7900   JAMES      CLERK  7698.0   3-Dec-81   950     NaN      30
12   7902    FORD    ANALYST  7566.0   3-Dec-81  3000     NaN      20
13   7934  MILLER      CLERK  7782.0  23-Jan-82  1300     NaN      10

     EMPNO   ENAME        JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
13   7934  MILLER      CLERK  7782.0  23-Jan-82  1300     NaN      10
6    7782   CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN      10
8    7839    KING  PRESIDENT     NaN  17-Nov-81  5000     NaN      10
0    7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20
10   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     NaN      20
3    7566   JONES    MANAGER  7839.0   2-Apr-81  2975     NaN      20
7    7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN      20
12   7902    FORD    ANALYST  7566.0   3-Dec-81  3000     NaN      20
11   7900   JAMES      CLERK  7698.0   3-Dec-81   950     NaN      30
2    7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30
4    7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
9    7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0      30
1    7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30
5    7698   BLAKE    MANAGER  7839.0   1-May-81  2850     NaN      30

"""