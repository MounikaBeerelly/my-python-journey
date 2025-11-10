import os
os.system("cls")

import pandas as pd

employeeDataFrame = pd.read_excel("C:\Practice\my-python-journey\DataSets\Excel files\Pandas.xlsx", sheet_name = "EmpData")
departmentDataFrame = pd.read_excel("C:\Practice\my-python-journey\DataSets\Excel files\Pandas.xlsx", sheet_name = "DeptData")

print("\nEmployee data loaded successfully...", end="\n")
print("\n", employeeDataFrame, end="\n")

print("\nDepartment data loaded successfully...", end="\n")
print("\n", departmentDataFrame, end="\n")
"""
Output:
=======

Employee data loaded successfully...

     EMPNO   ENAME        JOB     MGR   HIREDATE  HIRETIME   SAL    COMM  DEPTNO
0    7369   SMITH      CLERK  7902.0 1980-12-12  08:15:45   800     NaN      20
1    7499   ALLEN   SALESMAN  7698.0 1981-02-20  09:17:35  1600   300.0      30
2    7521    WARD   SALESMAN  7698.0 1981-02-22  10:20:15  1250   500.0      30
3    7566   JONES    MANAGER  7839.0 1981-04-02  10:15:25  2975     NaN      20
4    7654  MARTIN   SALESMAN  7698.0 1981-09-28  09:25:05  1250  1400.0      30
5    7698   BLAKE    MANAGER  7839.0 1981-05-01  11:15:55  2850     NaN      30
6    7782   CLARK    MANAGER  7839.0 1981-06-09  14:15:45  2450     NaN      10
7    7788   SCOTT    ANALYST  7566.0 1982-12-09  14:15:35  3000     NaN      20
8    7839    KING  PRESIDENT     NaN 1981-11-17  15:15:15  5000     NaN      10
9    7844  TURNER   SALESMAN  7698.0 1981-09-08  17:35:45  1500     0.0      30
10   7876   ADAMS      CLERK  7788.0 1983-01-12  11:15:25  1100     NaN      20
11   7900   JAMES      CLERK  7698.0 1981-12-03  23:13:24   950     NaN      30
12   7902    FORD    ANALYST  7566.0 1981-12-03  12:05:45  3000     NaN      20
13   7934  MILLER      CLERK  7782.0 1982-01-23  09:15:45  1300     NaN      10

Department data loaded successfully...

    DEPTNO       DNAME       LOC
0      10  ACCOUNTING  NEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON

"""