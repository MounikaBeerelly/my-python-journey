import os
os.system("cls")

import pandas as pd
import numpy as np

empSearchList = []

columnIndex = 1

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

for columnLabels in empDataFrame.columns :
    print(str(columnIndex) + ". " + columnLabels)
    columnIndex += 1
    
columnLabelList = list(empDataFrame.columns)

sortColumn = input("\nPlease enter the column name on which the data has to be Sorted: ")

empDataFrame.sort_values(by = [sortColumn.upper()], inplace = True)
print("\n" + empDataFrame.to_string(columns = empDataFrame.columns, index = False), end="\n")


"""
Output:
-------
1. EMPNO
2. ENAME
3. JOB
4. MGR
5. HIREDATE
6. SAL
7. COMM
8. DEPTNO

Please enter the column name on which the data has to be Sorted: ENAME

 EMPNO  ENAME       JOB    MGR  HIREDATE  SAL   COMM  DEPTNO
  7876  ADAMS     CLERK 7788.0 12-Jan-83 1100    NaN      20
  7499  ALLEN  SALESMAN 7698.0 20-Feb-81 1600  300.0      30
  7698  BLAKE   MANAGER 7839.0  1-May-81 2850    NaN      30
  7782  CLARK   MANAGER 7839.0  9-Jun-81 2450    NaN      10
  7902   FORD   ANALYST 7566.0  3-Dec-81 3000    NaN      20
  7900  JAMES     CLERK 7698.0  3-Dec-81  950    NaN      30
  7566  JONES   MANAGER 7839.0  2-Apr-81 2975    NaN      20
  7839   KING PRESIDENT    NaN 17-Nov-81 5000    NaN      10
  7654 MARTIN  SALESMAN 7698.0 28-Sep-81 1250 1400.0      30
  7934 MILLER     CLERK 7782.0 23-Jan-82 1300    NaN      10
  7788  SCOTT   ANALYST 7566.0  9-Dec-82 3000    NaN      20
  7369  SMITH     CLERK 7902.0 17-Dec-80  800    NaN      20
  7844 TURNER  SALESMAN 7698.0  8-Sep-81 1500    0.0      30
  7521   WARD  SALESMAN 7698.0 22-Feb-81 1250  500.0      30
  
  """