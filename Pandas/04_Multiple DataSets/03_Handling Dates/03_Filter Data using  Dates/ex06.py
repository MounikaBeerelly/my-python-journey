import os
os.system("cls")

import pandas as pd

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

print("\nThe data is loaded successfully, redirecting the data to the console...", end = "\n")
print("\n", empDataFrame, end="\n")

empDataFrame["HIREDATE"] = pd.to_datetime(empDataFrame["HIREDATE"], format = '%d-%b-%y')
empDataFrame["HIRETIME"] = pd.to_datetime(empDataFrame["HIRETIME"], format = '%H:%M:%S').dt.time

empHireFilter = empDataFrame[empDataFrame["HIREDATE"].dt.year == 1981]
empHireFilter = empHireFilter[empHireFilter["HIREDATE"].dt.month == 12]

print("\nThe number of employees matching to year 1981 with December month are : ", empHireFilter["EMPNO"].count(), end="\n")

"""
Output:
-------
The data is loaded successfully, redirecting the data to the console...

     EMPNO   ENAME        JOB     MGR   HIREDATE  HIRETIME   SAL    COMM  DEPTNO
0    7369   SMITH      CLERK  7902.0  17-Dec-80   8:15:45   800     NaN      20
1    7499   ALLEN   SALESMAN  7698.0  20-Feb-81   9:17:35  1600   300.0      30
2    7521    WARD   SALESMAN  7698.0  22-Feb-81  10:20:15  1250   500.0      30
3    7566   JONES    MANAGER  7839.0   2-Apr-81  10:15:25  2975     NaN      20
4    7654  MARTIN   SALESMAN  7698.0  28-Sep-81   9:25:05  1250  1400.0      30
5    7698   BLAKE    MANAGER  7839.0   1-May-81  11:15:55  2850     NaN      30
6    7782   CLARK    MANAGER  7839.0   9-Jun-81  14:15:45  2450     NaN      10
7    7788   SCOTT    ANALYST  7566.0   9-Dec-82  14:15:35  3000     NaN      20
8    7839    KING  PRESIDENT     NaN  17-Nov-81  15:15:15  5000     NaN      10
9    7844  TURNER   SALESMAN  7698.0   8-Sep-81  17:35:45  1500     0.0      30
10   7876   ADAMS      CLERK  7788.0  12-Jan-83  11:15:25  1100     NaN      20
11   7900   JAMES      CLERK  7698.0   3-Dec-81  23:13:24   950     NaN      30
12   7902    FORD    ANALYST  7566.0   3-Dec-81  12:05:45  3000     NaN      20
13   7934  MILLER      CLERK  7782.0  23-Jan-82   9:15:45  1300     NaN      10

The number of employees matching to year 1981 with December month are :  2

"""