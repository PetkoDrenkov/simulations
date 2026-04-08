import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.special import jv

''' 
parameters r_0, w_0 and v are meant to be changed with the constraint: r_0 >> w_0,
where v is topological charge (and order) of the beam (bessel function),
r_0 is radius and w_0 is thickness of the beam's fourier image (a ring)
'''

r_0 = 4
w_0 = 0.2
v = 1
r = np.linspace(0., 30, 5000)
p = np.linspace(0,2*np.pi,5000)
R, P = np.meshgrid(r, p)
X, Y = R*np.cos(P), R*np.sin(P)

N =  (w_0**2 / 2) * np.exp(1j*v*(P-np.pi/2))

E = N * np.exp(-(w_0*R/2)**2) * jv(v,R*r_0)
I = np.abs(E)**2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, I, cmap=cm.cividis)
fig.savefig(f'bgb_v={v}_r0={r_0}_w0={w_0}.png')
plt.show()
