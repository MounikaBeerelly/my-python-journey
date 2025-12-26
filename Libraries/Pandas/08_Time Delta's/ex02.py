import os
os.system("cls")

import pandas as pd

timedeltaObject = pd.Timedelta(4, unit = 'h')

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
                
            
"""
Output:
=======

The format of the calendar returned is:  0 days 04:00:00

"""