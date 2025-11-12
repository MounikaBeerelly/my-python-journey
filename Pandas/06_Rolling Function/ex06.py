import os
os.system("cls")

import numpy as np
import pandas as pd

productsDataframe = pd.read_csv("C:\Practice\my-python-journey\DataSets\ProductsData.csv")

prodDataFrame = productsDataframe[["Name", "Brand", "Price"]]

print("\n", prodDataFrame, end="\n")

rolledData = prodDataFrame["Price"].rolling(window = 3)

print("\n", rolledData.aggregate("sum"), end="\n")

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

 0        NaN
1        NaN
2      994.0
3      850.0
4      349.0
5      548.0
6      495.0
7      653.0
8      681.0
9     1458.0
10    1556.0
11    1323.0
12    1167.0
13    1189.0
14    1069.0
Name: Price, dtype: float64
"""

