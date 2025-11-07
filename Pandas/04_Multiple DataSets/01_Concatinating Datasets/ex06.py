import os
os.system("cls")

import pandas as pd
import numpy as np

empDept10DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\Joins\EmpDataSetDept10.csv")
    
print("\n", empDept10DataFrame, end="\n")

empDept20DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\Joins\EmpDataSetDept20.csv")
    
print("\n", empDept20DataFrame, end="\n")

empDept30DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\Joins\EmpDataSetDept30.csv")
    
print("\n", empDept30DataFrame, end="\n")

empDataFrames = [empDept10DataFrame, empDept20DataFrame, empDept30DataFrame]

finalEmpConcatData = pd.concat(empDataFrames, axis = 1, join = 'outer', ignore_index = True)

print("\n", finalEmpConcatData, end="\n")


"""
Output:
-------
 
    EMPNO   ENAME        JOB   SAL  DEPTNO
0   7782   CLARK    MANAGER  2450      10
1   7839    KING  PRESIDENT  5000      10
2   7934  MILLER      CLERK  1300      10

    EMPNO  ENAME      JOB   SAL  DEPTNO
0   7369  SMITH    CLERK   800      20
1   7566  JONES  MANAGER  2975      20
2   7788  SCOTT  ANALYST  3000      20
3   7782  CLARK  MANAGER  2450      10
4   7876  ADAMS    CLERK  1100      20
5   7902   FORD  ANALYST  3000      20

    EMPNO   ENAME       JOB   SAL  DEPTNO
0   7499   ALLEN  SALESMAN  1600      30
1   7521    WARD  SALESMAN  1250      30
2   7788   SCOTT   ANALYST  3000      20
3   7654  MARTIN  SALESMAN  1250      30
4   7698   BLAKE   MANAGER  2850      30
5   7876   ADAMS     CLERK  1100      20
6   7844  TURNER  SALESMAN  1500      30
7   7902    FORD   ANALYST  3000      20
8   7900   JAMES     CLERK   950      30

        0       1          2       3     4       5      6        7       8     9     10      11        12    13  14
0  7782.0   CLARK    MANAGER  2450.0  10.0  7369.0  SMITH    CLERK   800.0  20.0  7499   ALLEN  SALESMAN  1600  30
1  7839.0    KING  PRESIDENT  5000.0  10.0  7566.0  JONES  MANAGER  2975.0  20.0  7521    WARD  SALESMAN  1250  30
2  7934.0  MILLER      CLERK  1300.0  10.0  7788.0  SCOTT  ANALYST  3000.0  20.0  7788   SCOTT   ANALYST  3000  20
3     NaN     NaN        NaN     NaN   NaN  7782.0  CLARK  MANAGER  2450.0  10.0  7654  MARTIN  SALESMAN  1250  30
4     NaN     NaN        NaN     NaN   NaN  7876.0  ADAMS    CLERK  1100.0  20.0  7698   BLAKE   MANAGER  2850  30
5     NaN     NaN        NaN     NaN   NaN  7902.0   FORD  ANALYST  3000.0  20.0  7876   ADAMS     CLERK  1100  20
6     NaN     NaN        NaN     NaN   NaN     NaN    NaN      NaN     NaN   NaN  7844  TURNER  SALESMAN  1500  30
7     NaN     NaN        NaN     NaN   NaN     NaN    NaN      NaN     NaN   NaN  7902    FORD   ANALYST  3000  20
8     NaN     NaN        NaN     NaN   NaN     NaN    NaN      NaN     NaN   NaN  7900   JAMES     CLERK   950  30

"""