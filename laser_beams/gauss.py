import numpy as np
"""
When setting inputs of the func, k and w_0 should be strictly positive!
When using outputs of the func, they are ordered like in the return statement.
gg = pure gaussian(2,900) 
X = gg[0]
Y = gg[1]
I = gg[2]
g_00 = gg[3]
w_0 = gg[4]
"""

def pure_gaussian(w_0,k,z=0):
    r = np.linspace(-5, 5, 100)
    p = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(r, p)
    z_r = (k*w_0**2)/2
    w = w_0 * np.sqrt(1 + (z/z_r)**2)

    g_00 = ((w_0/w) * np.exp(-(X**2 + Y**2)/w**2) *
            np.exp(1j*(k*z + np.atan(z/z_r) +z*k*(X**2 + Y**2)/(z_r**2+z**2))))
    I = np.abs(g_00)**2
    return X, Y, I, g_00, w_0
