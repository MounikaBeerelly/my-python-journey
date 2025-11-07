import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-07', end = '2025-11-14')

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print(datesDataframe)

"""
Output:
------
The range of dates generated between two dates on daily frequency by default...
DatetimeIndex(['2025-11-07', '2025-11-08', '2025-11-09', '2025-11-10',
               '2025-11-11', '2025-11-12', '2025-11-13', '2025-11-14'],
              dtype='datetime64[ns]', freq='D')

"""