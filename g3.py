import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure
from scipy import integrate

w = 1
b = 0.5


t = np.linspace(-1, 1, 20)
x, v = np.meshgrid(t, t)

def dxdv(x, v):
    dx = v
    dv = -b*v - w**2 * x
    return dx, dv

def energy(x, v):
    return x**2 + v**2

dx, dv = dxdv(x, v)
E = energy(x, v)


fig = Figure(figsize=(6, 6), x_label="Displacement (m)", y_label="Velocity (m/s)")
fig.quiver(x, v, dx, dv, pivot='mid', label=r"")
fig.contour(x, v, E)
fig.streamplot(x, v, dx, dv)
# fig.legend()