import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


r = np.linspace(0, 2, 100)
p = np.linspace(0, 2*np.pi, 1000)
R, P = np.meshgrid(r, p)
g_00 = np.exp(-R**2)

X, Y = R*np.cos(P), R*np.sin(P)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, g_00,cmap=cm.cividis)
fig.savefig('gb.png')
plt.show()
