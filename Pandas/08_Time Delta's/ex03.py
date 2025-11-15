import os
os.system("cls")

import pandas as pd

timedeltaObject = pd.Timedelta(days = 2)

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
                
            
"""
Output:
=======

The format of the calendar returned is:  2 days 00:00:00
"""