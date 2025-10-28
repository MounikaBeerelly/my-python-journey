import os
os.system("cls")

import pandas as pd

empDataFrame = pd.DataFrame()

print(f"\nPrinting the empty data frame, thet is created...", end="\n")
print(empDataFrame)

empNumberList = [7369, 7499, 7521, 7566, 7654, 7698, 7782, 7788, 7839, 7844, 7876, 7900, 7902, 7934]

empDataFrame = pd.DataFrame(empNumberList)

print(f"\nPrinting the employees dat frame, loaded with employee numbers as a column...", end="\n")
print(empDataFrame)


"""
Output:
-------
Printing the empty data frame, thet is created...
Empty DataFrame
Columns: []
Index: []

Printing the employees dat frame, loaded with employee numbers as a column...
       0
0   7369
1   7499
2   7521
3   7566
4   7654
5   7698
6   7782
7   7788
8   7839
9   7844
10  7876
11  7900
12  7902
13  7934
"""