import numpy as np
"""
When setting inputs of the func, k and w_0 should be strictly positive.
When using outputs of the func, they are ordered like in the return statement. For example:
g = pure gaussian(0.002,5905249)
grid: x = g[0]; y = g[1]
intensity: i_gb = g[2]
amplitude: g_00 = g[3]
radius of the waist: w_0 = g[4]
wavenumber: (k = 2*pi/ wavelength): k = g[5]
z-axis: z = g[6]
beam radius: w = g[7]
"""

def pure_gaussian(w_0,k,z=0):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z_r = (k*w_0**2)/2
    w = w_0 * np.sqrt(1 + (z/z_r)**2)
    ph = (w_0/w) * np.exp(1j*(k*z + np.atan(z/z_r) +z*k*(x**2 + y**2)/(z_r**2 + z**2)))
    
    g_00 = ph * np.exp(-(x**2 + y**2)/w**2)

    i_gb = np.abs(g_00)**2
    
    return x, y, i_gb, g_00, w_0, k, z, w
