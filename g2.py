import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

start, end = -2, 2
dim = 101
step = 5
q = 1

x, y = np.meshgrid(np.linspace(start, end, dim), np.linspace(start, end, dim))
z = q / (x**2 + y**2)

u, v = np.gradient(z)

x_sliced = x[::step, ::step]
y_sliced = y[::step, ::step]
u_sliced = u[::step, ::step]
v_sliced = v[::step, ::step]

fig = Figure(figsize=(6, 6), xlim=[start, end], ylim=[start, end], x_label=r"$x$ (arb. units)", y_label=r"$y$ (arb. units)")
fig.quiver(x_sliced, y_sliced, u_sliced, v_sliced, pivot='tail', label=r"", scale=100)
fig.contourf(x, y, z, 2)
fig.legend()

