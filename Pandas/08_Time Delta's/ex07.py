import os
os.system("cls")

import pandas as pd

dateTimeSeries = pd.Series(pd.date_range('2025-11-15', periods = 10, freq = 'D'))

timeDeltaSeries = pd.Series([pd.Timedelta(days = dayIndex) for dayIndex in range(10)])

timeDeltaDataFrame = pd.DataFrame(dict(DateValues = dateTimeSeries, UnitApplied = timeDeltaSeries))

print("\n", timeDeltaDataFrame, end="\n")

timeDeltaDataFrame['NextLevelDate'] = timeDeltaDataFrame['DateValues'] + timeDeltaDataFrame['UnitApplied']

print("\n", timeDeltaDataFrame, end="\n")

"""
Output:
-------
   DateValues UnitApplied
0 2025-11-15      0 days
1 2025-11-16      1 days
2 2025-11-17      2 days
3 2025-11-18      3 days
4 2025-11-19      4 days
5 2025-11-20      5 days
6 2025-11-21      6 days
7 2025-11-22      7 days
8 2025-11-23      8 days
9 2025-11-24      9 days

   DateValues UnitApplied NextLevelDate
0 2025-11-15      0 days    2025-11-15 
1 2025-11-16      1 days    2025-11-17 
2 2025-11-17      2 days    2025-11-19 
3 2025-11-18      3 days    2025-11-21 
4 2025-11-19      4 days    2025-11-23 
5 2025-11-20      5 days    2025-11-25 
6 2025-11-21      6 days    2025-11-27 
7 2025-11-22      7 days    2025-11-29 
8 2025-11-23      8 days    2025-12-01 
9 2025-11-24      9 days    2025-12-03
"""