import os
os.system("cls")

import pandas as pd

empData = [
    [7369,'SMITH','CLERK',7902,800,None,20],
    [7499,'ALLEN','SALESMAN',7698,1600,300,30],
    [7521,'WARD','SALESMAN',7698,1250,500,30],
    [7566,'JONES','MANAGER',7839,2975,None,20],
    [7654,'MARTIN','SALESMAN',7698,1250,1400,30],
    [7698,'BLAKE','MANAGER',7839,2850,None,30,],
    [7782,'CLARK','MANAGER',7839,2450,None,10],
    [7788,'SCOTT','ANALYST',7566,3000,None,20],
    [7839,'KING','PRESIDENT',None,5000,None,10],
    [7844,'TURNER','SALESMAN',7698,1500,0,30],
    [7876,'ADAMS','CLERK',7788,1100,None,20],
    [7900,'JAMES','CLERK',7698,950,None,30],
    [7902,'FORD','ANALYST',7566,3000,None,20],
    [7934,'MILLER','CLERK',7782,1300,None,10]
]
empDataFrame = pd.DataFrame(empData, columns=['Empno', 'Ename', 'EmpJob', 'EmpMgr', 'empSal', 'EmpComm', 'EmpDeptID'])

print(f"\nPrinting the employees data frame, loaded with employee data as a columns..", end="\n")
print(empDataFrame)


"""
Output:
-------
Printing the employees data frame, loaded with employee data as a columns..
    Empno   Ename     EmpJob  EmpMgr  empSal  EmpComm  EmpDeptID
0    7369   SMITH      CLERK  7902.0     800      NaN         20
1    7499   ALLEN   SALESMAN  7698.0    1600    300.0         30
2    7521    WARD   SALESMAN  7698.0    1250    500.0         30
3    7566   JONES    MANAGER  7839.0    2975      NaN         20
4    7654  MARTIN   SALESMAN  7698.0    1250   1400.0         30
5    7698   BLAKE    MANAGER  7839.0    2850      NaN         30
6    7782   CLARK    MANAGER  7839.0    2450      NaN         10
7    7788   SCOTT    ANALYST  7566.0    3000      NaN         20
8    7839    KING  PRESIDENT     NaN    5000      NaN         10
9    7844  TURNER   SALESMAN  7698.0    1500      0.0         30
10   7876   ADAMS      CLERK  7788.0    1100      NaN         20
11   7900   JAMES      CLERK  7698.0     950      NaN         30
12   7902    FORD    ANALYST  7566.0    3000      NaN         20
13   7934  MILLER      CLERK  7782.0    1300      NaN         10
"""