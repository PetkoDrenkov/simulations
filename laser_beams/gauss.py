import numpy as np
"""
output parameters (g = pure_gaussian(chosen_argument_values)):
grid: x = g[0]; y = g[1], z-axis: z = g[2], beam radius: w = g[3], wavenumber: k = g[4], waist: w_0 = g[5], intensity: i_g = g[6], amplitude: g_00 = g[7].
"""

def pure_gaussian(w_0,k,z=0.):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z_r = (k * w_0**2)/2
    w = w_0 * np.sqrt(1 + (z/z_r)**2)
    ph = (w_0/w) * np.exp(1j*(k*z + np.atan(z/z_r) + z*k*(x**2 + y**2)/(2* z_r**2 + 2* z**2)))
    
    g_00 = ph * np.exp(-(x**2 + y**2)/w**2)

    i_g = np.abs(g_00)**2
    
    return x, y, z, w, k, w_0, i_g, g_00

