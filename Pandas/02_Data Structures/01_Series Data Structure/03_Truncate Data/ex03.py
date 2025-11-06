import os
os.system("cls")

import pandas as pd
import numpy as np

empDataFrame = pd.read_csv("C:\Practice\my-python-journey\DataSets\EmpDataSet.csv", index_col = "EMPNO")
    
print("\nThe data is loaded successfully, redirecting the data to the console...", end="\n")

sortEmpData = empDataFrame["SAL"].sort_index()

print("\n", sortEmpData, end = "\n")

truncEmpData = sortEmpData.truncate(before = 7654, after = 7844)

print("\n", truncEmpData, end="\n")

"""
OUTPUT:
=======
The data is loaded successfully, redirecting the data to the console...

 EMPNO
7369     800
7499    1600
7521    1250
7566    2975
7654    1250
7698    2850
7782    2450
7788    3000
7839    5000
7844    1500
7876    1100
7900     950
7902    3000
7934    1300
Name: SAL, dtype: int64

 EMPNO
7654    1250
7698    2850
7782    2450
7788    3000
7839    5000
7844    1500
Name: SAL, dtype: int64
"""