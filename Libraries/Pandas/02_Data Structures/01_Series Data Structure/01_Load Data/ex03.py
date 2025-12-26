#! python3

import os
os.system("cls")

import pandas as pd

# Build Series from dictionaries

empDictionary = {
    '101': 'KING',
    '102': 'JIM',
    '103': 'JOCK',
    '104': 'SCOTT',
    '105': 'SMITH',
    '106': 'ADAMS',
    '107': 'MILLER',
    '108': 'FORD',
    '109': 'JOHN'
}
        
empnoSeries = pd.Series(empDictionary)

print("\nThe employee details captured are..", end="\n\n")
print(empnoSeries)


"""
Output:
------
The employee details captured are..

101      KING
102       JIM
103      JOCK
104     SCOTT
105     SMITH
106     ADAMS
107    MILLER
108      FORD
109      JOHN
dtype: object

"""