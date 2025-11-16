import os
os.system("cls")

import pandas as pd

dateTimeSeries = pd.Series(pd.date_range('2025-11-15', periods = 3, freq = 'D'))

timeDeltaSeries = pd.Series([pd.Timedelta(days = dayIndex) for dayIndex in range(3)])

timeDeltaDataFrame = pd.DataFrame(dict(DateValues = dateTimeSeries, UnitApplied = timeDeltaSeries))

print("\n", timeDeltaDataFrame, end="\n")

"""
Output:
-------
   DateValues UnitApplied
0 2025-11-15      0 days
1 2025-11-16      1 days
2 2025-11-17      2 days
"""