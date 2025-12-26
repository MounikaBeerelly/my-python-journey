import os
os.system("cls")

import pandas as pd

timedeltaObject = pd.Timedelta(weeks = 4, days = 2)

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
                
            
"""
Output:
=======

The format of the calendar returned is:  30 days 00:00:00

"""