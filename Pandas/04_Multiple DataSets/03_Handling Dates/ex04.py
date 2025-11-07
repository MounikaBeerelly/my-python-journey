import os
os.system("cls")

import numpy as np
import pandas as pd

datesDataframe = pd.date_range(start = '2025-11-07', periods = 14)

print("\nThe range of dates generated between two dates on daily frequency by default...", end="\n")

print("\n",datesDataframe, end="\n")

"""
Output:
------
The range of dates generated between two dates on daily frequency by default...

 DatetimeIndex(['2025-11-07', '2025-11-08', '2025-11-09', '2025-11-10',
               '2025-11-11', '2025-11-12', '2025-11-13', '2025-11-14',
               '2025-11-15', '2025-11-16', '2025-11-17', '2025-11-18',
               '2025-11-19', '2025-11-20'],
              dtype='datetime64[ns]', freq='D')
            
"""