import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

xline = np.sin(zline)
yline = np.cos(zline)
zline = np.linspace(0, 15, 1000)

ax.plot3D(xline, yline, zline, 'black')

xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
zdata = 15 * np.random.random(100)

print(ax.scatter3D(xdata, ydata, zdata, c=zdata, s=30, cmap='Greens'))
