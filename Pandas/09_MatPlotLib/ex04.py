import os
os.system("cls")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

plotXAxisData = pd.DataFrame(np.arange(0,10))
plotYAxisData = plotXAxisData ** 3
plotZAxisData = plotXAxisData ** 4
plotTempAxisData = plotXAxisData ** 5

plotChart = plt.figure()
plot3DChart = plotChart.add_subplot(111, projection = '3d')
plot3DChart.plot_wireframe(plotXAxisData, plotYAxisData, plotZAxisData, rstride = 20, cstride = 10)
plt.show() 
