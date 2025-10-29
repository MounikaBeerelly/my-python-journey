import os
os.system("cls")

import pandas as pd
import numpy as np

empID = [7369, 7499, 7521, 7566, 7654, 7698, 7782, 7788, 7839, 7844, 7876, 7900, 7902, 7934]
empName = ['SMITH', 'ALLEN', 'WARD', 'JONES', 'MARTIN', 'BLAKE', 'CLARK', 'SCOTT', 'KING', 'TURNER', 'ADAMS', 'JAMES', 'FORD', 'MILLER']
empJob = ['CLERK', 'SALESMAN', 'SALESMAN', 'MANAGER', 'SALESMAN', 'MANAGER', 'MANAGER', 'ANALYST', 'PRESIDENT', 'SALESMAN', 'CLERK', 'CLERK', 'ANALYST', 'CLERK']
empMgr = [7902, 7698, 7698, 7839, 7698, 7839, 7839, 7566, np.nan, 7698, 7788, 7698, 7566, 7782]
empHiredate = ['17-Dec-80', '20-Feb-81', '22-Feb-81', '2-Apr-81', '28-Sep-81', '1-May-81', '9-Jun-81', '9-Dec-82', '17-Nov-81', '8-Sep-81', '12-Jan-83', '3-Dec-81', '3-Dec-81', '23-Jan-82']
empSal = [800, 1600, 1250, 2975, 1250, 2850, 2450, 3000, 5000, 1500, 1100, 950, 3000, 1300]
empComm = [np.nan, 300, 500, np.nan, 1400, np.nan, np.nan, np.nan, np.nan, np.nan, 0, np.nan, np.nan, np.nan]
empDeptno = [20, 30, 30, 20, 30, 30, 10, 20, 10, 30, 20, 30, 20, 10]

empListTuples = list(zip(empID, empName, empJob, empMgr, empHiredate, empSal, empComm, empDeptno))

"""Converting list of tuples to dataframe"""

#Adding rows and column names to the dataframe
empDataFrame = pd.DataFrame(empListTuples, index = ['RowID1', 'RowID2', 'RowID3', 'RowID4', 'RowID5', 'RowID6', 'RowID7', 'RowID8', 'RowID9', 'RowID10', 'RowID11', 'RowID12', 'RowID13', 'RowID14'], columns = ['empNo', 'empName', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno'])

print("\nPrinting the Employee dataframe, loaded with Employee list of tuples converted to a data frame", end="\n")

print(empDataFrame)

"""
Output:
=======
Printing the Employee dataframe, loaded with Employee list of tuples converted to a data frame
         empNo empName        job     mgr   hiredate   sal    comm  deptno
RowID1    7369   SMITH      CLERK  7902.0  17-Dec-80   800     NaN      20
RowID2    7499   ALLEN   SALESMAN  7698.0  20-Feb-81  1600   300.0      30
RowID3    7521    WARD   SALESMAN  7698.0  22-Feb-81  1250   500.0      30
RowID4    7566   JONES    MANAGER  7839.0   2-Apr-81  2975     NaN      20
RowID5    7654  MARTIN   SALESMAN  7698.0  28-Sep-81  1250  1400.0      30
RowID6    7698   BLAKE    MANAGER  7839.0   1-May-81  2850     NaN      30
RowID7    7782   CLARK    MANAGER  7839.0   9-Jun-81  2450     NaN      10
RowID8    7788   SCOTT    ANALYST  7566.0   9-Dec-82  3000     NaN      20
RowID9    7839    KING  PRESIDENT     NaN  17-Nov-81  5000     NaN      10
RowID10   7844  TURNER   SALESMAN  7698.0   8-Sep-81  1500     NaN      30
RowID11   7876   ADAMS      CLERK  7788.0  12-Jan-83  1100     0.0      20
RowID12   7900   JAMES      CLERK  7698.0   3-Dec-81   950     NaN      30
RowID13   7902    FORD    ANALYST  7566.0   3-Dec-81  3000     NaN      20
RowID14   7934  MILLER      CLERK  7782.0  23-Jan-82  1300     NaN      10
"""