import numpy as np
from matplotlib import pyplot as plt
from plotter import Figure

start, end = 0, 2 * np.pi
dim = 101
step = 5
    


x, y = np.meshgrid(np.linspace(start, end, dim), np.linspace(start, end, dim))
u = np.cos(x) * y
v = np.sin(x) * x

x_sliced = x[::step, ::step]
y_sliced = y[::step, ::step]
u_sliced = u[::step, ::step]
v_sliced = v[::step, ::step]

fig = Figure(figsize=(6, 6), xlim=[start, end], ylim=[start, end], x_label=r"$x$ (arb. units)", y_label=r"$y$ (arb. units)")
fig.quiver(x_sliced, y_sliced, u_sliced, v_sliced, pivot='mid', label=r"$u=cos(x)*y$, $v=sin(x)*x$")
fig.legend(loc='upper right')


