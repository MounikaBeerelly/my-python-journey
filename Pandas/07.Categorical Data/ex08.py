import os
os.system("cls")

import pandas as pd

myFruits01 = pd.Series(["Apple", "Banana", "Litchi", "Apple", "Orange", "Papaya", "Litchi"], dtype = "category")
print("\nThe identified fruits are: \n", myFruits01, end="\n")

myFruits01 = myFruits01.cat.remove_categories(["Apple"])

print("\nThe identified fruits are... \n", myFruits01, end = "\n")

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
dtype: category
Categories (5, object): ['Apple', 'Banana', 'Litchi', 'Orange', 'Papaya']

The identified fruits are...
 0       NaN
1    Banana
2    Litchi
3       NaN
4    Orange
5    Papaya
6    Litchi
dtype: category
Categories (4, object): ['Banana', 'Litchi', 'Orange', 'Papaya']
"""