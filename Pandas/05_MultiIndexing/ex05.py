import os
os.system("cls")

import pandas as pd

productsDataframe = pd.read_csv("C:\Practice\my-python-journey\DataSets\ProductsData.csv")

# print("\n", productsDataframe , end="\n")

"""AGGREGATION FUNCTIONS"""

print("\nThe total price of the products is: ", end="\n")
print(productsDataframe["Price"].sum(), end="\n")

print("\nThe maximum price of the products is: ", end="\n")
print(productsDataframe["Price"].max(), end="\n")

print("\nThe minimum price of the products is: ", end="\n")
print(productsDataframe["Price"].min(), end="\n")

print("\nThe average price of the products is: ", end="\n")
print(productsDataframe["Price"].mean(), end="\n")

print("\nThe median price of the products is: ", end="\n")
print(productsDataframe["Price"].median(), end="\n")

print("\nThe number price of the products are: ", end="\n")
print(productsDataframe["Price"].count(), end="\n")

print("\nThe mode of the products are: ", end="\n")
print(productsDataframe["Price"].mode(), end="\n")

print("\nThe standard deviation of the products are: ", end="\n")
print(productsDataframe["Price"].std(), end="\n")

print("\nThe absolute values of the products are: ", end="\n")
print(productsDataframe["Price"].abs(), end="\n")

print("\nThe product of price of the products are: ", end="\n")
print(productsDataframe["Price"].prod(), end="\n")

print("\nThe cumulative sum of the products are: ", end="\n")
print(productsDataframe["Price"].cumsum(), end="\n")

print("\nThe cumulative product of the products are: ", end="\n")
print(productsDataframe["Price"].cumprod(), end="\n")

print("\nThe total descriptive statistics of the products are... ", end="\n")
print(productsDataframe["Price"].describe(), end="\n")

"""
Output:
-------

The total price of the products is:
4615

The maximum price of the products is:
845

The minimum price of the products is:
1

The average price of the products is:
307.6666666666667

The median price of the products is:
257.0

The number price of the products are:
15

The mode of the products are:
0       1
1      68
2     101
3     121
4     159
5     221
6     227
7     257
8     265
9     279
10    426
11    454
12    502
13    689
14    845
Name: Price, dtype: int64

The standard deviation of the products are:
235.68946478263257

The absolute values of the products are:
0     265
1     502
2     227
3     121
4       1
5     426
6      68
7     159
8     454
9     845
10    257
11    221
12    689
13    279
14    101
Name: Price, dtype: int64

The product of price of the products are:
-7977679707989502624

The cumulative sum of the products are:
0      265
1      767
2      994
3     1115
4     1116
5     1542
6     1610
7     1769
8     2223
9     3068
10    3325
11    3546
12    4235
13    4514
14    4615
Name: Price, dtype: int64

The cumulative product of the products are:
0                     265
1                  133030
2                30197810
3              3653935010
4              3653935010
5           1556576314260
6         105847189369680
7       16829703109779120
8     7640685211839720480
9       18578206220740000
10    4774598998730180000
11    3721966517925337888
12     337504604930130208
13    1930064406958569952
14   -7977679707989502624
Name: Price, dtype: int64

The total descriptive statistics of the products are...
count     15.000000
mean     307.666667
std      235.689465
min        1.000000
25%      140.000000
50%      257.000000
75%      440.000000
max      845.000000
Name: Price, dtype: float64
"""