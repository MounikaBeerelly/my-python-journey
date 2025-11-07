import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-01', end = '2025-11-10', periods = 10)

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print(datesDataframe[1 :])

"""
OUTPUT:
=======

The range of dates generated between two dates on daily frequency by default...
DatetimeIndex(['2025-11-02', '2025-11-03', '2025-11-04', '2025-11-05',
               '2025-11-06', '2025-11-07', '2025-11-08', '2025-11-09',
               '2025-11-10'],
              dtype='datetime64[ns]', freq=None)

"""