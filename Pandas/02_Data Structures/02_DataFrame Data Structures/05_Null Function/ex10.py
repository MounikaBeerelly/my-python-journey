import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
    
print("\nThe data is loaded successfully, redirecting the data to the console...", end="\n")

print(empDataFrame)

nullFillRule = input("\nDo you want to fill null values in the data frame(Y OR NO): ")

empDataFrameCopy = pd.DataFrame(empDataFrame)

if nullFillRule == 'Y' or nullFillRule == 'y' :
   print("\n", empDataFrameCopy.fillna(method="pad"))
else :
    print("\n", empDataFrame)

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

Do you want to fill null values in the data frame(Y OR NO): y
C:\Practice\my-python-journey\Pandas\02_Data Structures\02_DataFrame Data Structures\05_Null Function\ex10.py:18: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  print("\n", empDataFrameCopy.fillna(method="pad"))

     EMPNO   ENAME        JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
0    7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20
1    7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30
2    7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30
3    7566   JONES    MANAGER  7839.0   2-Apr-81  2975   500.0      20
4    7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
5    7698   BLAKE    MANAGER  7839.0   1-May-81  2850  1400.0      30
6    7782   CLARK    MANAGER  7839.0   9-Jun-81  2450  1400.0      10
7    7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000  1400.0      20
8    7839    KING  PRESIDENT  7566.0  17-Nov-81  5000  1400.0      10
9    7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0      30
10   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     0.0      20
11   7900   JAMES      CLERK  7698.0   3-Dec-81   950     0.0      30
12   7902    FORD    ANALYST  7566.0   3-Dec-81  3000     0.0      20
13   7934  MILLER      CLERK  7782.0  23-Jan-82  1300     0.0      10
"""