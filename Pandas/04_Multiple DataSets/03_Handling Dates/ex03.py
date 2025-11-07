import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-07', end = '2025-11-14', periods = 14)

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print(datesDataframe)

"""
Output:
------

The range of dates generated between two dates on daily frequency by default...
DatetimeIndex([          '2025-11-07 00:00:00',
               '2025-11-07 12:55:23.076923076',
               '2025-11-08 01:50:46.153846153',
               '2025-11-08 14:46:09.230769230',
               '2025-11-09 03:41:32.307692307',
               '2025-11-09 16:36:55.384615384',
               '2025-11-10 05:32:18.461538461',
               '2025-11-10 18:27:41.538461538',
               '2025-11-11 07:23:04.615384615',
               '2025-11-11 20:18:27.692307692',
               '2025-11-12 09:13:50.769230769',
               '2025-11-12 22:09:13.846153846',
               '2025-11-13 11:04:36.923076923',
                         '2025-11-14 00:00:00'],
              dtype='datetime64[ns]', freq=None)
"""