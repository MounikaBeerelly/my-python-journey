import os
os.system("cls")

import pandas as pd

myFruits = pd.Series(["Apple", "Banana", "Litchi", "Apple", "Orange", "Papaya", "Litchi"])

print("\nThe identified fruits are: \n", myFruits, end="\n")

"""
Output:
-------
The identified fruits are:
 0     Apple
1    Banana
2    Litchi
3     Apple
4    Orange
5    Papaya
6    Litchi
dtype: object
"""