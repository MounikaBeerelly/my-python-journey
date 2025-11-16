import os
os.system("cls")

import numpy as np
import pandas as pd

plotDataFrame = pd.DataFrame(np.random.randn(10,5), index = pd.date_range('11/1/2025', periods = 10), columns = list('PQRST'))

print("\n", plotDataFrame, end="\n")

plotDataFrame.plot()

"""
Output:
=======

"""