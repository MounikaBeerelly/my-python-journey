import os
os.system("cls")

import pandas as pd

empDataFrame = pd.DataFrame()

print(f"\nPrinting the empty data frame, thet is created...", end="\n")
print(empDataFrame)

# Adding labels
empNumberDictionary = {
    'Empno' : [7369, 7499, 7521, 7566, 7654, 7698, 7782, 7788, 7839, 7844, 7876, 7900, 7902, 7934],
    'EmpName' : ['SMITH', 'ALLEN', 'WARD', 'JONES', 'MARTIN', 'BLAKE', 'CLARK', 'SCOTT', 'KING', 'TURNER', 'ADAMS', 'JAMES', 'FORD', 'MILLER'],
    'EmpJob' : ['CLERK', 'SALESMAN', 'SALESMAN', 'MANAGER', 'SALESMAN', 'MANAGER', 'MANAGER', 'ANALYST', 'PRESIDENT', 'SALESMAN', 'CLERK', 'CLERK', 'ANALYST', 'CLERK']
}

empDataFrame = pd.DataFrame(empNumberDictionary)

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
    Empno EmpName     EmpJob
0    7369   SMITH      CLERK
1    7499   ALLEN   SALESMAN
2    7521    WARD   SALESMAN
3    7566   JONES    MANAGER
4    7654  MARTIN   SALESMAN
5    7698   BLAKE    MANAGER
6    7782   CLARK    MANAGER
7    7788   SCOTT    ANALYST
8    7839    KING  PRESIDENT
9    7844  TURNER   SALESMAN
10   7876   ADAMS      CLERK
11   7900   JAMES      CLERK
12   7902    FORD    ANALYST
13   7934  MILLER      CLERK
"""