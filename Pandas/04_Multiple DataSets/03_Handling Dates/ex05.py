import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(end = '2025-11-07', periods = 14)

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print("\n",datesDataframe, end="\n")

"""
Output:
------
The range of dates generated between two dates on daily frequency by default...

 DatetimeIndex(['2025-10-25', '2025-10-26', '2025-10-27', '2025-10-28',
               '2025-10-29', '2025-10-30', '2025-10-31', '2025-11-01',
               '2025-11-02', '2025-11-03', '2025-11-04', '2025-11-05',
               '2025-11-06', '2025-11-07'],
              dtype='datetime64[ns]', freq='D')

"""