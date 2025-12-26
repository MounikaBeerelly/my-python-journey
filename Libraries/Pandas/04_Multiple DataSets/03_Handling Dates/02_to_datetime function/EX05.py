import os
os.system("cls")

import pandas as pd

pd.set_option('display.max_columns', None)

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

print("\nThe data is loaded successfully, redirecting the data to the console...", end = "\n")
print("\n", empDataFrame, end="\n")

empDataFrame["HIREDATE"] = pd.to_datetime(empDataFrame["HIREDATE"], format = '%d-%b-%y')

empDataFrame['HIREYEAR'] = empDataFrame['HIREDATE'].dt.year
empDataFrame['HIREMONTH'] = empDataFrame['HIREDATE'].dt.month
empDataFrame['HIREDAY'] = empDataFrame['HIREDATE'].dt.day
empDataFrame['HIREHOUR'] = empDataFrame['HIREDATE'].dt.hour
empDataFrame['HIREMINUTE'] = empDataFrame['HIREDATE'].dt.minute
empDataFrame['HIRESECOND'] = empDataFrame['HIREDATE'].dt.second

print("\n", empDataFrame, end="\n")

"""
Output:
------

     EMPNO   ENAME        JOB     MGR   HIREDATE   SAL  ...  HIREYEAR  HIREMONTH  HIREDAY  HIREHOUR  HIREMINUTE  HIRESECOND
0    7369   SMITH      CLERK  7902.0 1980-12-17   800  ...      1980         12       17         0           0           0
1    7499   ALLEN   SALESMAN  7698.0 1981-02-20  1600  ...      1981          2       20         0           0           0
2    7521    WARD   SALESMAN  7698.0 1981-02-22  1250  ...      1981          2       22         0           0           0
3    7566   JONES    MANAGER  7839.0 1981-04-02  2975  ...      1981          4        2         0           0           0
4    7654  MARTIN   SALESMAN  7698.0 1981-09-28  1250  ...      1981          9       28         0           0           0
5    7698   BLAKE    MANAGER  7839.0 1981-05-01  2850  ...      1981          5        1         0           0           0
6    7782   CLARK    MANAGER  7839.0 1981-06-09  2450  ...      1981          6        9         0           0           0
7    7788   SCOTT    ANALYST  7566.0 1982-12-09  3000  ...      1982         12        9         0           0           0
8    7839    KING  PRESIDENT     NaN 1981-11-17  5000  ...      1981         11       17         0           0           0
9    7844  TURNER   SALESMAN  7698.0 1981-09-08  1500  ...      1981          9        8         0           0           0
10   7876   ADAMS      CLERK  7788.0 1983-01-12  1100  ...      1983          1       12         0           0           0
11   7900   JAMES      CLERK  7698.0 1981-12-03   950  ...      1981         12        3         0           0           0
12   7902    FORD    ANALYST  7566.0 1981-12-03  3000  ...      1981         12        3         0           0           0
13   7934  MILLER      CLERK  7782.0 1982-01-23  1300  ...      1982          1       23         0           0           0

[14 rows x 14 columns]
"""