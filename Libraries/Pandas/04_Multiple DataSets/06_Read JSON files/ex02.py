import os
os.system("cls")

import pandas as pd

# reading json file
departmentDataFrame = pd.read_json("C:\Practice\my-python-journey\DataSets\JSON files\DeptDataSet.json")

print("\n", departmentDataFrame, end="\n")

"""
Output:
=======

    Deptno    DeptName       Loc
0      10  ACCOUNTING  MEW YORK
1      20    RESEARCH    DALLAS
2      30       SALES   CHICAGO
3      40  OPERATIONS    BOSTON
"""