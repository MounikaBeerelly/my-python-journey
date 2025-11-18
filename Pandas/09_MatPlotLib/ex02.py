import os
os.system("cls")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plotXAxisData = pd.DataFrame(np.arange(0,10))
plotYAxisData = plotXAxisData ** 3

plt.title("This is the Chart Title")
plt.xlabel("Event Time")
plt.ylabel("Event Temperature")
plt.plot(plotXAxisData, plotYAxisData, 'r')
plt.plot(plotXAxisData, plotYAxisData, 'o')
plt.show()
