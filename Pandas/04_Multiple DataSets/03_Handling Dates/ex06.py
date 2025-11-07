import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-01', end = '2025-11-20', periods = 5)

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print(datesDataframe)

"""
Output:
------
The range of dates generated between two dates on daily frequency by default...
DatetimeIndex(['2025-11-01 00:00:00', '2025-11-05 18:00:00',
               '2025-11-10 12:00:00', '2025-11-15 06:00:00',
               '2025-11-20 00:00:00'],
              dtype='datetime64[ns]', freq=None)
              
"""