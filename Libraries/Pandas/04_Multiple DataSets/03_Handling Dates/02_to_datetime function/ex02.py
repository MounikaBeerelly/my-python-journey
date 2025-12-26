import os
os.system("cls")

import pandas as pd

inDateAsString = input("\nPlease enter any date in your format : ")

inDateTime = pd.to_datetime(inDateAsString)

print(f"\nThe given date in string format {inDateAsString} represented as Date and Time is :", inDateTime, end="\n")


"""
Output:
------

Please enter any date in your format : november 10 2025
The given date in string format november 10 2025 represented as Date and Time is : 2025-11-10 00:00:00

Please enter any date in your format : 2025, nov 10th
The given date in string format 2025, nov 10th represented as Date and Time is : 2025-11-10 00:00:00


Please enter any date in your format : 1st of december 2025
The given date in string format 1st of december 2025 represented as Date and Time is : 2025-12-01 00:00:00
"""

