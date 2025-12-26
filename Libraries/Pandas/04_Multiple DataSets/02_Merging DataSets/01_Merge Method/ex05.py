import os
os.system("cls")

import pandas as pd
import numpy as np


deptDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\DeptDataSet.csv")
    
print("\n", deptDataFrame, end="\n")

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
    
print("\n", empDataFrame, end="\n")

empDeptJoinInfo = pd.merge(deptDataFrame, empDataFrame, how = 'outer', on = ['DEPTNO'])

print("\n", empDeptJoinInfo, end="\n")

"""
Output:
-------

    DEPTNO       DNAME       LOC
0      10  ACCOUNTING  NEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON

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

     DEPTNO       DNAME       LOC   EMPNO   ENAME        JOB     MGR   HIREDATE     SAL    COMM
0       10  ACCOUNTING  NEW YORK  7782.0   CLARK    MANAGER  7839.0   9-Jun-81  2450.0     NaN
1       10  ACCOUNTING  NEW YORK  7839.0    KING  PRESIDENT     NaN  17-Nov-81  5000.0     NaN
2       10  ACCOUNTING  NEW YORK  7934.0  MILLER      CLERK  7782.0  23-Jan-82  1300.0     NaN
3       20    RESEARCH    DALLAS  7369.0   SMITH      CLERK  7902.0  17-Dec-80   800.0     NaN
4       20    RESEARCH    DALLAS  7566.0   JONES    MANAGER  7839.0   2-Apr-81  2975.0     NaN
5       20    RESEARCH    DALLAS  7788.0   SCOTT    ANALYST  7566.0   9-Dec-82  3000.0     NaN
6       20    RESEARCH    DALLAS  7876.0   ADAMS      CLERK  7788.0  12-Jan-83  1100.0     NaN
7       20    RESEARCH    DALLAS  7902.0    FORD    ANALYST  7566.0   3-Dec-81  3000.0     NaN
8       30       SALES   CHICAGO  7499.0   ALLEN   SALESMAN  7698.0  20-Feb-81  1600.0   300.0
9       30       SALES   CHICAGO  7521.0    WARD   SALESMAN  7698.0  22-Feb-81  1250.0   500.0
10      30       SALES   CHICAGO  7654.0  MARTIN   SALESMAN  7698.0  28-Sep-81  1250.0  1400.0
11      30       SALES   CHICAGO  7698.0   BLAKE    MANAGER  7839.0   1-May-81  2850.0     NaN
12      30       SALES   CHICAGO  7844.0  TURNER   SALESMAN  7698.0   8-Sep-81  1500.0     0.0
13      30       SALES   CHICAGO  7900.0   JAMES      CLERK  7698.0   3-Dec-81   950.0     NaN
14      40  OPERATIONS    BOSTON     NaN     NaN        NaN     NaN        NaN     NaN     NaN

"""