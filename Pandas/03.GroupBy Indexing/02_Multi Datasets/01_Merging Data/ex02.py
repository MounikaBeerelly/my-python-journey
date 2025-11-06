import os
os.system("cls")

import pandas as pd
import numpy as np

pd.set_option('display.float_format','{:.0f}'.format)

empDept10DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\ImbalancedDataSet\EmpDataSetDept10.csv")
    
print("\n", empDept10DataFrame, end="\n")

empDept20DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\ImbalancedDataSet\EmpDataSetDept20.csv")
    
print("\n", empDept20DataFrame, end="\n")

empDept30DataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\ImbalancedDataSet\EmpDataSetDept30.csv")
    
print("\n", empDept30DataFrame, end="\n")

empDataFrames = [empDept10DataFrame, empDept20DataFrame, empDept30DataFrame]

finalEmpConcatData = pd.concat(empDataFrames)

print("\n", finalEmpConcatData, end="\n")


"""
Output:
-------

    EMPNO   ENAME        JOB  MGR   HIREDATE   SAL  COMM     CONTACT  DEPTNO
0   7782   CLARK    MANAGER 7839   9-Jun-81  2450   NaN  9876543210      10
1   7839    KING  PRESIDENT  NaN  17-Nov-81  5000   NaN  8765432190      10
2   7934  MILLER      CLERK 7782  23-Jan-82  1300   NaN  7654321098      10

    EMPNO  ENAME      JOB   MGR   HIREDATE   SAL  COMM            EMAIL  DEPTNO
0   7369  SMITH    CLERK  7902  17-Dec-80   800   NaN  smith@gmail.com      20
1   7566  JONES  MANAGER  7839   2-Apr-81  2975   NaN  jones@gmail.com      20
2   7788  SCOTT  ANALYST  7566   9-Dec-82  3000   NaN  scott@gmail.com      20
3   7876  ADAMS    CLERK  7788  12-Jan-83  1100   NaN  adams@gmail.com      20
4   7902   FORD  ANALYST  7566   3-Dec-81  3000   NaN   ford@gmail.com      20

    EMPNO   ENAME       JOB   MGR   HIREDATE   SAL  COMM  DEPTNO
0   7499   ALLEN  SALESMAN  7698  20-Feb-81  1600   300      30
1   7521    WARD  SALESMAN  7698  22-Feb-81  1250   500      30
2   7654  MARTIN  SALESMAN  7698  28-Sep-81  1250  1400      30
3   7698   BLAKE   MANAGER  7839   1-May-81  2850   NaN      30
4   7844  TURNER  SALESMAN  7698   8-Sep-81  1500     0      30
5   7900   JAMES     CLERK  7698   3-Dec-81   950   NaN      30

    EMPNO   ENAME        JOB  MGR   HIREDATE   SAL  COMM    CONTACT  DEPTNO            EMAIL
0   7782   CLARK    MANAGER 7839   9-Jun-81  2450   NaN 9876543210      10              NaN
1   7839    KING  PRESIDENT  NaN  17-Nov-81  5000   NaN 8765432190      10              NaN
2   7934  MILLER      CLERK 7782  23-Jan-82  1300   NaN 7654321098      10              NaN
0   7369   SMITH      CLERK 7902  17-Dec-80   800   NaN        NaN      20  smith@gmail.com
1   7566   JONES    MANAGER 7839   2-Apr-81  2975   NaN        NaN      20  jones@gmail.com
2   7788   SCOTT    ANALYST 7566   9-Dec-82  3000   NaN        NaN      20  scott@gmail.com
3   7876   ADAMS      CLERK 7788  12-Jan-83  1100   NaN        NaN      20  adams@gmail.com
4   7902    FORD    ANALYST 7566   3-Dec-81  3000   NaN        NaN      20   ford@gmail.com
0   7499   ALLEN   SALESMAN 7698  20-Feb-81  1600   300        NaN      30              NaN
1   7521    WARD   SALESMAN 7698  22-Feb-81  1250   500        NaN      30              NaN
2   7654  MARTIN   SALESMAN 7698  28-Sep-81  1250  1400        NaN      30              NaN
3   7698   BLAKE    MANAGER 7839   1-May-81  2850   NaN        NaN      30              NaN
4   7844  TURNER   SALESMAN 7698   8-Sep-81  1500     0        NaN      30              NaN
5   7900   JAMES      CLERK 7698   3-Dec-81   950   NaN        NaN      30              NaN
"""