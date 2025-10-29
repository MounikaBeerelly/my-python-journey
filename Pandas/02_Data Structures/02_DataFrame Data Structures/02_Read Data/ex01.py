import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv")

empHeadData = empDataFrame.head()

print("\nPrinting the Employees data...", end="\n")
print(empHeadData)

"""
Note:
-----
1. read_csv() method automatically loads the data into a Python variable as a data frame, converting the variable to the dataframe object
2. We can call all the data frame methods on the DataFrame object after loading the data in the file.
3. When we are applying the "head()" method without any supplied arguments, then by default Pandas will read first 5 records.
4. All the data is missing in the data file is loaded by default as "NaN". 
"""


"""
Output:
=======
Printing the Employees data...
   EMPNO   ENAME       JOB     MGR   HIREDATE   SAL    COMM  DEPTNO
0   7369   SMITH     CLERK  7902.0  17-Dec-80   800     NaN      20
1   7499   ALLEN  SALESMAN  7698.0  20-Feb-81  1600   300.0      30
2   7521    WARD  SALESMAN  7698.0  22-Feb-81  1250   500.0      30
3   7566   JONES   MANAGER  7839.0   2-Apr-81  2975     NaN      20
4   7654  MARTIN  SALESMAN  7698.0  28-Sep-81  1250  1400.0      30

"""