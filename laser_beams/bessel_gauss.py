import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.special import jv

''' 
parameters r_0, w_0 and v are meant to be changed with the constraint: r_0 >> w_0,
where v is topological charge (and order) of the beam (bessel function),
r_0 is radius and w_0 is thickness of the beam's fourier image (a ring)
'''

def bessel_gauss(r_0, w_0, v):

    r = np.linspace(0., 7, 100)
    p = np.linspace(0,2*np.pi,100)
    R, P = np.meshgrid(r, p)
    X, Y = R*np.cos(P), R*np.sin(P)

    N =  (w_0**2/2) * np.exp(1j*v*(P-np.pi/2))

    E = N * np.exp(-(w_0*R/2)**2) * jv(v,R*r_0)
    I = np.abs(E)**2
    return X, Y, I, r_0, w_0, v, E
