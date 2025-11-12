import os
os.system("cls")

import numpy as np
import pandas as pd

productsDataframe = pd.read_csv("C:\Practice\my-python-journey\DataSets\ProductsData.csv")

prodDataFrame = productsDataframe[["Name", "Brand", "Price"]]

print("\n", prodDataFrame, end="\n")

rolledData = prodDataFrame.rolling(window = 3)

print("\n", rolledData["Price"].aggregate(["sum", "mean"]), end="\n")

"""
Output:
--------

                                               Name                         Brand  Price
0             Compact Printer Air Advanced Digital       Garner, Boyle and Flynn    265
1                                           Tablet                   Mueller Inc    502
2                             Smart Blender Cooker    Lawson, Keller and Winters    227
3                     Advanced Router Rechargeable            Gallagher and Sons    121
4                     Portable Mouse Monitor Phone                     Irwin LLC      1
5                                            Radio  Benjamin, Nelson and Hancock    426
6   Ultra Projector Oven Thermostat Prime Advanced        Mccoy, Waters and Rose     68
7                               Webcam Stove Grill               Morrow and Sons    159
8                                        Eco Radio  Edwards, Odonnell and Conley    454
9                Ultra Powerbank Brush Charger Max   Brennan, Archer and Rosales    845
10                                   Wireless Dock                    Russo-West    257
11                    Fast Camera Router Fan Smart              Vazquez and Sons    221
12                                    Heater Radio             Delgado-Blackwell    689
13                     Smart Trimmer Webcam Heater                 Contreras PLC    279
14                              Webcam Dock Heater     Juarez, Powell and Travis    101

        sum        mean
0      NaN         NaN
1      NaN         NaN
2    994.0  331.333333
3    850.0  283.333333
4    349.0  116.333333
5    548.0  182.666667
6    495.0  165.000000
7    653.0  217.666667
8    681.0  227.000000
9   1458.0  486.000000
10  1556.0  518.666667
11  1323.0  441.000000
12  1167.0  389.000000
13  1189.0  396.333333
14  1069.0  356.333333
"""

