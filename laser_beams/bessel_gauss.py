import numpy as np
from scipy.special import jv

def bessel_gauss(w_0,k,k_tr,v=0,z=0):

    r = np.linspace(0., 17, 100)
    p = np.linspace(0,2*np.pi,100)
    r, p = np.meshgrid(r, p)
    x, y = r*np.cos(p), r*np.sin(p)
    z *= 0.001

    # Rayleigh diffraction length: depends on wavelength (wavenumber) and beam waist
    z_R = (k*w_0**2)/2

    # beam wavefront radius of curvature
    R = np.divide((z**2 +z_R**2), z)

    # beam radius
    w = w_0 * np.sqrt(1 + (z/z_R)**2)

    # Gouy phase shift
    gouy = np.atan(z/z_R)

    # the point of these 2 rows is to make code look less messy
    u =  (-1/w**2 + 1j*k/(2*R))*(r**2 + k_tr**2 * z**2 / k**2)
    o =  k_tr*r/(1 + 1j*z/z_R)

    # electric field amplitude(first row) and intensity(next row)
    j_v = np.exp(1j*(k - k_tr**2/(2*k))*z - 1j*gouy) * jv(v, o) * np.exp(u)
    i_bgb = np.abs(j_v)**2

    return x, y, z, v, w_0, z_R, i_bgb, j_v


