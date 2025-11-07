import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-01', periods = 5, freq = pd.offsets.MonthEnd(5))

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print(datesDataframe)

"""
OUTPUT:
=======

The range of dates generated between two dates on daily frequency by default...
DatetimeIndex(['2025-11-30', '2026-04-30', '2026-09-30', '2027-02-28',
               '2027-07-31'],
              dtype='datetime64[ns]', freq='5ME')

"""