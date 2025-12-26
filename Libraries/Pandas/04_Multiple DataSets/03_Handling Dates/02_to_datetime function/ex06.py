import os
os.system("cls")

import pandas as pd

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

print("\nThe data is loaded successfully, redirecting the data to the console...", end = "\n")
print("\n", empDataFrame, end="\n")

empDataFrame["HIREDATE"] = pd.to_datetime(empDataFrame["HIREDATE"], format = '%d-%b-%y')
empDataFrame["HIRETIME"] = pd.to_datetime(empDataFrame["HIRETIME"], format = '%H:%M:%S')
#empDataFrame["HIRETIME"] = pd.to_datetime(empDataFrame["HIRETIME"], format = '%H:%M:%S').dt.time

empDataFrame['HIREYEAR'] = empDataFrame['HIREDATE'].dt.year
empDataFrame['HIREMONTH'] = empDataFrame['HIREDATE'].dt.month
empDataFrame['HIREDAY'] = empDataFrame['HIREDATE'].dt.day
empDataFrame['HIREHOUR'] = empDataFrame['HIRETIME'].dt.hour
empDataFrame['HIREMINUTE'] = empDataFrame['HIRETIME'].dt.minute
empDataFrame['HIRESECOND'] = empDataFrame['HIRETIME'].dt.second

print("\n", empDataFrame, end="\n")

"""
Output:
=======

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

     EMPNO   ENAME        JOB     MGR   HIREDATE            HIRETIME  ...  HIREYEAR  HIREMONTH  HIREDAY  HIREHOUR  HIREMINUTE  HIRESECOND
0    7369   SMITH      CLERK  7902.0 1980-12-17 1900-01-01 08:15:45  ...      1980         12       17         8          15          45
1    7499   ALLEN   SALESMAN  7698.0 1981-02-20 1900-01-01 09:17:35  ...      1981          2       20         9          17          35
2    7521    WARD   SALESMAN  7698.0 1981-02-22 1900-01-01 10:20:15  ...      1981          2       22        10          20          15
3    7566   JONES    MANAGER  7839.0 1981-04-02 1900-01-01 10:15:25  ...      1981          4        2        10          15          25
4    7654  MARTIN   SALESMAN  7698.0 1981-09-28 1900-01-01 09:25:05  ...      1981          9       28         9          25           5
5    7698   BLAKE    MANAGER  7839.0 1981-05-01 1900-01-01 11:15:55  ...      1981          5        1        11          15          55
6    7782   CLARK    MANAGER  7839.0 1981-06-09 1900-01-01 14:15:45  ...      1981          6        9        14          15          45
7    7788   SCOTT    ANALYST  7566.0 1982-12-09 1900-01-01 14:15:35  ...      1982         12        9        14          15          35
8    7839    KING  PRESIDENT     NaN 1981-11-17 1900-01-01 15:15:15  ...      1981         11       17        15          15          15
9    7844  TURNER   SALESMAN  7698.0 1981-09-08 1900-01-01 17:35:45  ...      1981          9        8        17          35          45
10   7876   ADAMS      CLERK  7788.0 1983-01-12 1900-01-01 11:15:25  ...      1983          1       12        11          15          25
11   7900   JAMES      CLERK  7698.0 1981-12-03 1900-01-01 23:13:24  ...      1981         12        3        23          13          24
12   7902    FORD    ANALYST  7566.0 1981-12-03 1900-01-01 12:05:45  ...      1981         12        3        12           5          45
13   7934  MILLER      CLERK  7782.0 1982-01-23 1900-01-01 09:15:45  ...      1982          1       23         9          15          45

[14 rows x 15 columns]
"""