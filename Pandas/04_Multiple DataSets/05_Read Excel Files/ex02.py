import os
os.system("cls")

import pandas as pd

sheetName = input("\nPlease enter the excel sheet name to load : ")

loadedDataFrame = pd.read_excel("C:\Practice\my-python-journey\DataSets\Excel files\Pandas.xlsx", sheet_name = sheetName)

print("\n", loadedDataFrame, end="\n")

"""
Output:
=======
Please enter the excel sheet name to load : DeptData

    DEPTNO       DNAME       LOC
0      10  ACCOUNTING  NEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON
"""