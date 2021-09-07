import numpy as np
import matplotlib.pyplot as plt

ax = plt.axes(projection='3d')

xline = np.sin(zline)
yline = np.cos(zline)
zline = np.linspace(0, 15, 1000)

ax.plot3D(xline, yline, zline, 'white')
