import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")
    
print("\n", empDataFrame, end="\n")

empPhoneSeries = pd.Series([9876543210, 8765432109, 7654321098, 6543210987, 5432109876, 4321098765, 3210987653, 5432109876, 5432109876, 4321098765, 1234567890, 9876543210, 8765432109, 7654321098], name = "CONTACT")

print("\n", empPhoneSeries, end="\n")

finalEmpConcatData = pd.concat([empDataFrame, empPhoneSeries], axis = 1)

print("\n", finalEmpConcatData, end="\n")


"""
Output:
-------

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

 0     9876543210
1     8765432109
2     7654321098
3     6543210987
4     5432109876
5     4321098765
6     3210987653
7     5432109876
8     5432109876
9     4321098765
10    1234567890
11    9876543210
12    8765432109
13    7654321098
Name: CONTACT, dtype: int64

     EMPNO   ENAME        JOB     MGR   HIREDATE   SAL    COMM  DEPTNO     CONTACT
0    7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20  9876543210
1    7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30  8765432109
2    7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30  7654321098
3    7566   JONES    MANAGER  7839.0   2-Apr-81  2975     NaN      20  6543210987
4    7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30  5432109876
5    7698   BLAKE    MANAGER  7839.0   1-May-81  2850     NaN      30  4321098765
6    7782   CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN      10  3210987653
7    7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN      20  5432109876
8    7839    KING  PRESIDENT     NaN  17-Nov-81  5000     NaN      10  5432109876
9    7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0      30  4321098765
10   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     NaN      20  1234567890
11   7900   JAMES      CLERK  7698.0   3-Dec-81   950     NaN      30  9876543210
12   7902    FORD    ANALYST  7566.0   3-Dec-81  3000     NaN      20  8765432109
13   7934  MILLER      CLERK  7782.0  23-Jan-82  1300     NaN      10  7654321098

"""