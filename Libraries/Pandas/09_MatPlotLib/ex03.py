import os
os.system("cls")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plotXAxisData = pd.DataFrame(np.arange(0,10))
plotYAxisData = plotXAxisData ** 3
plotZAxisData = plotXAxisData ** 4
plotTempAxisData = plotXAxisData ** 5

plt.title("This is the Chart Title")
plt.xlabel("Event Time")
plt.ylabel("Event Temperature")
# plt.plot(plotXAxisData, plotYAxisData, 'r')
# plt.plot(plotXAxisData, plotYAxisData, 'o')
plt.plot(plotXAxisData, plotYAxisData)
plt.annotate(xy = [3, 4], text = "safe Zone")
plt.annotate(xy = [6, 8], text = "Red Zone")
plt.plot(plotXAxisData, plotZAxisData)
plt.plot(plotXAxisData, plotTempAxisData)
plt.legend(["Trial 01", "Trial 02", "Trial 03"], loc = 1)
plt.style.use('dark_background')
plt.plot(plotXAxisData, plotZAxisData)
plt.show()
