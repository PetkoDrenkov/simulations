import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.special import jv

v = 1
r_0 = 1
r = np.linspace(0, 30, 5000)
p = np.linspace(0, 2*np.pi, 5000)
R, P = np.meshgrid(r, p)

Z = jv(v,R*r_0)
X, Y = R*np.cos(P), R*np.sin(P)
I = Z**2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, I,cmap=cm.cividis)
fig.savefig(f'bb_v={v}_r0={r_0}.png')
plt.show()
