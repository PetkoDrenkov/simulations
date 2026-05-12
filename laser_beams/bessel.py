import numpy as np
from scipy.special import jv


def bessel(k,k_tr,v=0,z=0):
    r = np.linspace(0, 100, 100)
    p = np.linspace(0, 2*np.pi, 100)
    r, p = np.meshgrid(r, p)
    x, y = r*np.cos(p), r*np.sin(p)


    j_v = np.exp(1j * np.sqrt(k**2 - k_tr**2) * z) * jv(v,r*k_tr)
    i_b = np.abs(j_v)**2
    return x, y, z, v, j_v, i_b




