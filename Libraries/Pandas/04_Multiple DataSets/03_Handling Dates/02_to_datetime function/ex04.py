import os
os.system("cls")

from datetime import datetime

import pandas as pd

inCurrentDateTime = datetime.now()

print("\nThe current date and time captured is : ", inCurrentDateTime)

print("\nPresenting the Date for Tomorrow : ", inCurrentDateTime + pd.to_timedelta(1, unit = 'D'))
print("\nPresenting the Date for next Month : ", inCurrentDateTime + pd.DateOffset(months = 1))
print("\nPresenting the Date for next year : ", inCurrentDateTime + pd.DateOffset(years = 1))

"""
Output:
------
The current date and time captured is :  2025-11-07 16:32:31.509954

Presenting the Date for Tomorrow :  2025-11-08 16:32:31.509954

Presenting the Date for next Month :  2025-12-07 16:32:31.509954

Presenting the Date for next year :  2026-11-07 16:32:31.509954
"""