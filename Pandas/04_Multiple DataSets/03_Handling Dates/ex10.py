import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-01', periods = 10, tz = 'Asia/Kolkata')

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print(datesDataframe)

"""
OUTPUT:
=======

The range of dates generated between two dates on daily frequency by default...
DatetimeIndex(['2025-11-01 00:00:00+05:30', '2025-11-02 00:00:00+05:30',
               '2025-11-03 00:00:00+05:30', '2025-11-04 00:00:00+05:30',
               '2025-11-05 00:00:00+05:30', '2025-11-06 00:00:00+05:30',
               '2025-11-07 00:00:00+05:30', '2025-11-08 00:00:00+05:30',
               '2025-11-09 00:00:00+05:30', '2025-11-10 00:00:00+05:30'],
              dtype='datetime64[ns, Asia/Kolkata]', freq='D')

"""