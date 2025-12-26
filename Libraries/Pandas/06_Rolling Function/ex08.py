import os
os.system("cls")

import numpy as np
import pandas as pd

productsDataframe = pd.read_csv("C:\Practice\my-python-journey\DataSets\ProductsData.csv")

prodDataFrame = productsDataframe[["Name", "Brand", "Price"]]

print("\n", prodDataFrame, end="\n")

expandedData = prodDataFrame.expanding(min_periods = 3)

print("\n", expandedData["Price"].aggregate(["sum", "mean"]), end="\n")

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
3   1115.0  278.750000
4   1116.0  223.200000
5   1542.0  257.000000
6   1610.0  230.000000
7   1769.0  221.125000
8   2223.0  247.000000
9   3068.0  306.800000
10  3325.0  302.272727
11  3546.0  295.500000
12  4235.0  325.769231
13  4514.0  322.428571
14  4615.0  307.666667
"""

