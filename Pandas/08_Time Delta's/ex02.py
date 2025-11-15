import os
os.system("cls")

import pandas as pd

timedeltaObject = pd.Timedelta(4, unit = 'h')

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
                
            
"""
Output:
=======

The format of the calendar returned is:  4 days 03:25:45
"""