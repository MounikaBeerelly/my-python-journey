import os
os.system("cls")

import pandas as pd
import numpy as np

empDept10DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\BalancedDataSet\EmpDataSetDept10.csv")
    
print("\n", empDept10DataFrame, end="\n")

empDept20DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\BalancedDataSet\EmpDataSetDept20.csv")
    
print("\n", empDept20DataFrame, end="\n")

empDept30DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\BalancedDataSet\EmpDataSetDept30.csv")
    
print("\n", empDept30DataFrame, end="\n")

empDataFrames = [empDept10DataFrame, empDept20DataFrame, empDept30DataFrame]

finalEmpConcatData = pd.concat(empDataFrames)

print("\n", finalEmpConcatData, end="\n")


"""
Output:
-------

    EMPNO   ENAME        JOB     MGR   HIREDATE   SAL  COMM  DEPTNO
0   7782   CLARK    MANAGER  7839.0   9-Jun-81  2450   NaN      10
1   7839    KING  PRESIDENT     NaN  17-Nov-81  5000   NaN      10
2   7934  MILLER      CLERK  7782.0  23-Jan-82  1300   NaN      10

    EMPNO  ENAME      JOB   MGR   HIREDATE   SAL  COMM  DEPTNO
0   7369  SMITH    CLERK  7902  17-Dec-80   800   NaN      20
1   7566  JONES  MANAGER  7839   2-Apr-81  2975   NaN      20
2   7788  SCOTT  ANALYST  7566   9-Dec-82  3000   NaN      20
3   7876  ADAMS    CLERK  7788  12-Jan-83  1100   NaN      20
4   7902   FORD  ANALYST  7566   3-Dec-81  3000   NaN      20

    EMPNO   ENAME       JOB   MGR   HIREDATE   SAL    COMM  DEPTNO
0   7499   ALLEN  SALESMAN  7698  20-Feb-81  1600   300.0      30
1   7521    WARD  SALESMAN  7698  22-Feb-81  1250   500.0      30
2   7654  MARTIN  SALESMAN  7698  28-Sep-81  1250  1400.0      30
3   7698   BLAKE   MANAGER  7839   1-May-81  2850     NaN      30
4   7844  TURNER  SALESMAN  7698   8-Sep-81  1500     0.0      30
5   7900   JAMES     CLERK  7698   3-Dec-81   950     NaN      30

    EMPNO   ENAME        JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
0   7782   CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN      10
1   7839    KING  PRESIDENT     NaN  17-Nov-81  5000     NaN      10
2   7934  MILLER      CLERK  7782.0  23-Jan-82  1300     NaN      10
0   7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20
1   7566   JONES    MANAGER  7839.0   2-Apr-81  2975     NaN      20
2   7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN      20
3   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     NaN      20
4   7902    FORD    ANALYST  7566.0   3-Dec-81  3000     NaN      20
0   7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30
1   7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30
2   7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
3   7698   BLAKE    MANAGER  7839.0   1-May-81  2850     NaN      30
4   7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     0.0      30
5   7900   JAMES      CLERK  7698.0   3-Dec-81   950     NaN      30

"""