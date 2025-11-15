import os
os.system("cls")

import pandas as pd

timedeltaObject = pd.Timedelta(weeks = 4, days = 2)

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
 
timedeltaObject = pd.Timedelta(days = 2, hours = 5, minutes = 20, seconds = 45)

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
               
timedeltaObject = pd.Timedelta(days = 2, hours = 5, minutes = 20, seconds = 45, milliseconds = 100, microseconds = 10000, nanoseconds = 2343)

print("\nThe format of the calendar returned is: ", timedeltaObject, end="\n")                               
                          
"""
Output:
=======


The format of the calendar returned is:  30 days 00:00:00

The format of the calendar returned is:  2 days 05:20:45

The format of the calendar returned is:  2 days 05:20:45.110002343
"""