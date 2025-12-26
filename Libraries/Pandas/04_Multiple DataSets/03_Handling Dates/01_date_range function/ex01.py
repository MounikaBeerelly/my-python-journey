import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range('07/11/2025', periods = 20, freq = 'h')

print("\nThe range of dates generated for every one hour on 7th November 2025 are...", end="\n")

print(datesDataframe)

"""
Output:
------

The range of dates generated for every one hour on 7th November 2025 are...
DatetimeIndex(['2025-07-11 00:00:00', '2025-07-11 01:00:00',
               '2025-07-11 02:00:00', '2025-07-11 03:00:00',
               '2025-07-11 04:00:00', '2025-07-11 05:00:00',
               '2025-07-11 06:00:00', '2025-07-11 07:00:00',
               '2025-07-11 08:00:00', '2025-07-11 09:00:00',
               '2025-07-11 10:00:00', '2025-07-11 11:00:00',
               '2025-07-11 12:00:00', '2025-07-11 13:00:00',
               '2025-07-11 14:00:00', '2025-07-11 15:00:00',
               '2025-07-11 16:00:00', '2025-07-11 17:00:00',
               '2025-07-11 18:00:00', '2025-07-11 19:00:00'],
              dtype='datetime64[ns]', freq='h')
"""