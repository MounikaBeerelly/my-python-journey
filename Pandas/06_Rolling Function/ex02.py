import os
os.system("cls")

import pandas as pd

productsDataframe = pd.read_csv("C:\Practice\my-python-journey\DataSets\ProductsData.csv")

prodDataFrame = productsDataframe[["Name", "Brand", "Price"]]

print("\n", prodDataFrame, end="\n")

rolledData = prodDataFrame["Price"].rolling(window = 3).mean()

print("\n", rolledData, end="\n")

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

 0            NaN
1            NaN
2     331.333333
3     283.333333
4     116.333333
5     182.666667
6     165.000000
7     217.666667
8     227.000000
9     486.000000
10    518.666667
11    441.000000
12    389.000000
13    396.333333
14    356.333333
Name: Price, dtype: float64

"""

